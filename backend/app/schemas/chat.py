"""
Chat Schemas
Pydantic models for chat requests and responses
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    """Individual chat message"""

    role: str = Field(
        ...,
        pattern="^(user|assistant)$",
        description="Message role: 'user' or 'assistant'"
    )

    content: str = Field(
        ...,
        min_length=1,
        description="Message content"
    )


class ChatRequest(BaseModel):
    """Schema for chat completion request"""

    conversation_id: Optional[str] = Field(
        None,
        description="Conversation ID (creates new conversation if None)"
    )

    message: str = Field(
        ...,
        min_length=1,
        max_length=10000,
        description="User message content"
    )

    use_web_search: bool = Field(
        default=True,
        description="Enable web search tool"
    )

    use_code_interpreter: bool = Field(
        default=True,
        description="Enable code interpreter tool"
    )

    reasoning_effort: str = Field(
        default="medium",
        pattern="^(low|medium|high)$",
        description="Reasoning effort level"
    )

    mcp_servers: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="List of MCP server configurations (passed directly to OpenAI API)"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "conversation_id": "123e4567-e89b-12d3-a456-426614174000",
                "message": "What's the weather like in Paris today?",
                "use_web_search": True,
                "use_code_interpreter": False,
                "reasoning_effort": "medium",
                "mcp_servers": None
            }]
        }
    }


class URLCitation(BaseModel):
    """Web search URL citation"""

    url: str = Field(..., description="Source URL")
    title: str = Field(..., description="Source title")
    start_index: Optional[int] = Field(None, description="Citation start index in text")
    end_index: Optional[int] = Field(None, description="Citation end index in text")


class UsageInfo(BaseModel):
    """Token usage information"""

    input_tokens: int = Field(..., description="Number of input tokens")
    output_tokens: int = Field(..., description="Number of output tokens")
    reasoning_tokens: Optional[int] = Field(None, description="Number of reasoning tokens")
    total_tokens: int = Field(..., description="Total tokens used")


class ChatResponse(BaseModel):
    """Schema for chat completion response"""

    message: str = Field(..., description="Assistant's response message")
    conversation_id: str = Field(..., description="Conversation ID")
    message_id: str = Field(..., description="Message ID")
    usage: UsageInfo = Field(..., description="Token usage information")
    citations: List[URLCitation] = Field(default_factory=list, description="Web search citations")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "message": "According to recent weather data, Paris is currently experiencing...",
                "conversation_id": "123e4567-e89b-12d3-a456-426614174000",
                "message_id": "456e7890-e89b-12d3-a456-426614174111",
                "usage": {
                    "input_tokens": 50,
                    "output_tokens": 200,
                    "reasoning_tokens": 100,
                    "total_tokens": 350
                },
                "citations": [
                    {
                        "url": "https://weather.com/paris",
                        "title": "Paris Weather Forecast"
                    }
                ],
                "metadata": {}
            }]
        }
    }


class StreamChatRequest(BaseModel):
    """Schema for streaming chat request"""

    conversation_id: Optional[str] = Field(
        None,
        description="Conversation ID (creates new conversation if None)"
    )

    messages: List[ChatMessage] = Field(
        ...,
        min_length=1,
        description="List of messages in the conversation"
    )

    use_web_search: bool = Field(
        default=True,
        description="Enable web search tool"
    )

    use_code_interpreter: bool = Field(
        default=True,
        description="Enable code interpreter tool"
    )

    reasoning_effort: str = Field(
        default="medium",
        pattern="^(low|medium|high)$",
        description="Reasoning effort level"
    )

    mcp_servers: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="List of MCP server configurations (passed directly to OpenAI API)"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "conversation_id": "123e4567-e89b-12d3-a456-426614174000",
                "messages": [
                    {"role": "user", "content": "Hello!"},
                    {"role": "assistant", "content": "Hi! How can I help you?"},
                    {"role": "user", "content": "Tell me about GPT-5"}
                ],
                "use_web_search": True,
                "use_code_interpreter": False,
                "reasoning_effort": "medium",
                "mcp_servers": None
            }]
        }
    }
