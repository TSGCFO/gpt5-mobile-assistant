"""
OpenAI Service
Complete integration with OpenAI GPT-5 Responses API
Includes: Web Search, Code Interpreter, Reasoning, Streaming
"""

from typing import List, Dict, Any, Optional, AsyncIterator
from openai import AsyncOpenAI, OpenAIError as OpenAIAPIError
from app.core.config import settings
from app.core.logging_config import get_logger
from app.core.exceptions import OpenAIError

logger = get_logger(__name__)


class OpenAIService:
    """
    Service for interacting with OpenAI GPT-5 Responses API.

    Features:
    - Standard and streaming responses
    - Web search with citations
    - Code interpreter (Python execution)
    - Configurable reasoning effort (low/medium/high)
    - Token usage tracking
    - Error handling and retries
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize OpenAI service.

        Args:
            api_key: OpenAI API key (uses settings if not provided)
        """
        self.api_key = api_key or settings.OPENAI_API_KEY
        self.client = AsyncOpenAI(api_key=self.api_key)
        self.default_model = settings.OPENAI_MODEL
        self.default_reasoning_effort = settings.OPENAI_REASONING_EFFORT
        logger.info(f"OpenAI service initialized with model: {self.default_model}")

    async def create_response(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        reasoning_effort: Optional[str] = None,
        use_web_search: bool = True,
        use_code_interpreter: bool = True,
        mcp_servers: Optional[List[Dict[str, Any]]] = None,
        max_output_tokens: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Create a single response using GPT-5 Responses API.

        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Model to use (defaults to configured model)
            reasoning_effort: Reasoning level: 'low', 'medium', or 'high'
            use_web_search: Enable web search tool
            use_code_interpreter: Enable code interpreter tool
            mcp_servers: List of MCP server configurations (passed directly to API)
            max_output_tokens: Maximum tokens to generate

        Returns:
            Dictionary containing response data:
            - output_text: The assistant's response text
            - usage: Token usage information
            - citations: Web search citations (if applicable)
            - output: Full output items from API

        Raises:
            OpenAIError: If API call fails
        """
        try:
            # Build tools array
            tools = []
            if use_web_search:
                tools.append({"type": "web_search"})

            if use_code_interpreter:
                tools.append({
                    "type": "code_interpreter",
                    "container": {"type": "auto"}
                })

            # Add MCP servers (OpenAI handles all MCP communication)
            if mcp_servers:
                tools.extend(mcp_servers)

            # Prepare request parameters
            request_params = {
                "model": model or self.default_model,
                "input": messages,
            }

            # Add reasoning configuration
            if reasoning_effort or self.default_reasoning_effort:
                request_params["reasoning"] = {
                    "effort": reasoning_effort or self.default_reasoning_effort
                }

            # Add tools if any
            if tools:
                request_params["tools"] = tools

            # Add max tokens if specified
            if max_output_tokens:
                request_params["max_output_tokens"] = max_output_tokens

            logger.info(
                f"Creating response with model={request_params['model']}, "
                f"reasoning_effort={request_params.get('reasoning', {}).get('effort')}, "
                f"tools={len(tools)}"
            )

            # Make API call
            response = await self.client.responses.create(**request_params)

            # Extract output text
            output_text = self._extract_output_text(response)

            # Extract citations (web search results)
            citations = self._extract_citations(response)

            # Extract usage information
            usage = {
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
                "reasoning_tokens": getattr(response.usage.output_tokens_details, "reasoning_tokens", None),
                "total_tokens": response.usage.total_tokens,
            }

            logger.info(
                f"Response created successfully. Tokens: {usage['total_tokens']} "
                f"(input: {usage['input_tokens']}, output: {usage['output_tokens']}, "
                f"reasoning: {usage['reasoning_tokens']})"
            )

            return {
                "output_text": output_text,
                "usage": usage,
                "citations": citations,
                "output": response.output,
            }

        except OpenAIAPIError as e:
            logger.error(f"OpenAI API error: {str(e)}")
            raise OpenAIError(
                message=f"Failed to create response: {str(e)}",
                details={"error_type": type(e).__name__}
            )
        except Exception as e:
            logger.error(f"Unexpected error in create_response: {str(e)}")
            raise OpenAIError(
                message="Unexpected error creating response",
                details={"error": str(e)}
            )

    async def create_streaming_response(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        reasoning_effort: Optional[str] = None,
        use_web_search: bool = True,
        use_code_interpreter: bool = True,
        mcp_servers: Optional[List[Dict[str, Any]]] = None,
        max_output_tokens: Optional[int] = None,
    ) -> AsyncIterator[Dict[str, Any]]:
        """
        Create a streaming response using GPT-5 Responses API.

        Args:
            messages: List of message dictionaries
            model: Model to use
            reasoning_effort: Reasoning level
            use_web_search: Enable web search
            use_code_interpreter: Enable code interpreter
            mcp_servers: List of MCP server configurations
            max_output_tokens: Maximum tokens

        Yields:
            Dictionary for each streaming event with:
            - type: Event type
            - delta: Text delta (for text events)
            - content: Full event content

        Raises:
            OpenAIError: If streaming fails
        """
        try:
            # Build tools array
            tools = []
            if use_web_search:
                tools.append({"type": "web_search"})

            if use_code_interpreter:
                tools.append({
                    "type": "code_interpreter",
                    "container": {"type": "auto"}
                })

            # Add MCP servers (OpenAI handles all MCP communication)
            if mcp_servers:
                tools.extend(mcp_servers)

            # Prepare request parameters
            request_params = {
                "model": model or self.default_model,
                "input": messages,
                "stream": True,
            }

            # Add reasoning
            if reasoning_effort or self.default_reasoning_effort:
                request_params["reasoning"] = {
                    "effort": reasoning_effort or self.default_reasoning_effort
                }

            # Add tools
            if tools:
                request_params["tools"] = tools

            # Add max tokens
            if max_output_tokens:
                request_params["max_output_tokens"] = max_output_tokens

            logger.info(f"Starting streaming response with model={request_params['model']}")

            # Create streaming response
            stream = await self.client.responses.create(**request_params)

            # Stream events
            async for event in stream:
                event_dict = {
                    "type": event.type if hasattr(event, "type") else "unknown",
                    "event": event,
                }

                # Extract delta for text events
                if hasattr(event, "delta"):
                    event_dict["delta"] = event.delta

                # Extract specific event data
                if event.type == "response.output_text.delta":
                    event_dict["text_delta"] = event.delta
                elif event.type == "response.output_text.done":
                    event_dict["text_done"] = True
                elif event.type == "response.completed":
                    event_dict["completed"] = True
                    if hasattr(event, "response") and hasattr(event.response, "usage"):
                        event_dict["usage"] = {
                            "input_tokens": event.response.usage.input_tokens,
                            "output_tokens": event.response.usage.output_tokens,
                            "total_tokens": event.response.usage.total_tokens,
                        }

                yield event_dict

            logger.info("Streaming response completed successfully")

        except OpenAIAPIError as e:
            logger.error(f"OpenAI streaming error: {str(e)}")
            yield {
                "type": "error",
                "error": str(e),
                "error_type": type(e).__name__
            }
        except Exception as e:
            logger.error(f"Unexpected streaming error: {str(e)}")
            yield {
                "type": "error",
                "error": "Unexpected streaming error",
                "details": str(e)
            }

    def _extract_output_text(self, response) -> str:
        """
        Extract plain text output from response.

        Args:
            response: OpenAI response object

        Returns:
            Extracted text or empty string
        """
        try:
            # Response API returns output as a list of items
            for item in response.output:
                if item.type == "message":
                    # Extract text from message content
                    for content in item.content:
                        if content.type == "output_text":
                            return content.text
            return ""
        except Exception as e:
            logger.warning(f"Failed to extract output text: {e}")
            return ""

    def _extract_citations(self, response) -> List[Dict[str, str]]:
        """
        Extract web search citations from response.

        Args:
            response: OpenAI response object

        Returns:
            List of citation dictionaries with url, title, etc.
        """
        citations = []
        try:
            for item in response.output:
                if item.type == "message":
                    for content in item.content:
                        if hasattr(content, "annotations"):
                            for annotation in content.annotations:
                                if annotation.type == "url_citation":
                                    citations.append({
                                        "url": annotation.url,
                                        "title": annotation.title,
                                        "start_index": annotation.start_index,
                                        "end_index": annotation.end_index,
                                    })
        except Exception as e:
            logger.warning(f"Failed to extract citations: {e}")

        return citations

    async def close(self):
        """Close the OpenAI client connection"""
        await self.client.close()
        logger.info("OpenAI client closed")


# Dependency for FastAPI
_openai_service: Optional[OpenAIService] = None


def get_openai_service() -> OpenAIService:
    """
    Get or create OpenAI service instance.
    Use as FastAPI dependency.

    Example:
        @app.post("/chat")
        async def chat(
            service: OpenAIService = Depends(get_openai_service)
        ):
            response = await service.create_response(messages)
            return response
    """
    global _openai_service
    if _openai_service is None:
        _openai_service = OpenAIService()
    return _openai_service
