/**
 * Chat API
 * Chat completion and streaming endpoints
 */

import apiClient from './client';
import { API_ENDPOINTS } from '@/constants/api';
import { ChatRequest, ChatResponse, Message } from '@/types/chat.types';

export const chatApi = {
  /**
   * Send a message and get response
   */
  async sendMessage(request: ChatRequest): Promise<ChatResponse> {
    const response = await apiClient.post<ChatResponse>(
      API_ENDPOINTS.CHAT_COMPLETIONS,
      request
    );
    return response.data;
  },

  /**
   * Stream chat completion (handled separately due to SSE)
   * This returns the fetch response for streaming
   */
  async streamMessage(
    request: {
      conversation_id?: string;
      messages: Array<{ role: string; content: string }>;
      use_web_search?: boolean;
      use_code_interpreter?: boolean;
      reasoning_effort?: string;
    },
    onChunk: (text: string) => void,
    onComplete: () => void,
    onError: (error: string) => void
  ): Promise<void> {
    const { API_BASE_URL } = await import('@/constants/api');
    const SecureStore = await import('expo-secure-store');

    try {
      // Get credentials
      const username = await SecureStore.getItemAsync('username');
      const password = await SecureStore.getItemAsync('password');

      if (!username || !password) {
        throw new Error('Not authenticated');
      }

      // Create Basic Auth header
      const credentials = btoa(`${username}:${password}`);

      // Use fetch for streaming
      const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.CHAT_STREAM}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Basic ${credentials}`,
        },
        body: JSON.stringify(request),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      // Read stream
      const reader = response.body?.getReader();
      const decoder = new TextDecoder();

      if (!reader) {
        throw new Error('No response body');
      }

      let buffer = '';

      while (true) {
        const { done, value } = await reader.read();

        if (done) break;

        buffer += decoder.decode(value, { stream: true });

        // Process complete SSE messages
        const lines = buffer.split('\n');
        buffer = lines.pop() || '';

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            try {
              const eventData = JSON.parse(line.slice(6));

              // Handle different event types
              if (eventData.type === 'response.output_text.delta') {
                onChunk(eventData.text_delta || eventData.delta || '');
              } else if (eventData.type === 'response.completed') {
                onComplete();
              } else if (eventData.type === 'error' || eventData.error) {
                onError(eventData.error || 'Streaming error');
              }
            } catch (parseError) {
              console.warn('Failed to parse SSE event:', parseError);
            }
          }
        }
      }
    } catch (error: any) {
      onError(error.message || 'Failed to stream message');
    }
  },

  /**
   * Get messages for a conversation
   */
  async getConversationMessages(
    conversationId: string,
    limit?: number,
    offset = 0
  ): Promise<Message[]> {
    const params = new URLSearchParams();
    if (limit) params.append('limit', limit.toString());
    params.append('offset', offset.toString());

    const response = await apiClient.get<Message[]>(
      `${API_ENDPOINTS.CONVERSATION_MESSAGES(conversationId)}?${params.toString()}`
    );

    return response.data;
  },
};

// Helper function for Base64 encoding
function btoa(str: string): string {
  return Buffer.from(str, 'binary').toString('base64');
}
