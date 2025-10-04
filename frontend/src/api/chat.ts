/**
 * Chat API
 * Chat completion and streaming endpoints
 */

import apiClient from './client';
import { API_ENDPOINTS } from '@/constants/api';
import { ChatRequest, ChatResponse, Message } from '@/types/chat.types';
// XMLHttpRequest is natively available in React Native for SSE streaming

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
   * Stream chat completion using Server-Sent Events (SSE)
   * Uses XMLHttpRequest (native to React Native) for reliable SSE streaming
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
    const { secureStorage } = await import('@/utils/secureStorage');

    try {
      // Get credentials
      const username = await secureStorage.getItem('username');
      const password = await secureStorage.getItem('password');

      if (!username || !password) {
        throw new Error('Not authenticated');
      }

      // Create Basic Auth header
      const credentials = btoa(`${username}:${password}`);

      // Use XMLHttpRequest for SSE streaming (native to React Native)
      const xhr = new XMLHttpRequest();

      xhr.open('POST', `${API_BASE_URL}${API_ENDPOINTS.CHAT_STREAM}`);
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.setRequestHeader('Authorization', `Basic ${credentials}`);

      let buffer = '';

      // Handle progressive response data
      xhr.onprogress = () => {
        const responseText = xhr.responseText;

        // Get only new data since last progress event
        const newData = responseText.substring(buffer.length);
        buffer = responseText;

        // Process SSE messages
        const lines = newData.split('\n');

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            try {
              const eventData = JSON.parse(line.slice(6));

              // Handle different event types
              if (eventData.type === 'response.output_text.delta') {
                onChunk(eventData.delta || '');
              } else if (eventData.type === 'response.completed') {
                onComplete();
              } else if (eventData.type === 'error') {
                onError(eventData.error || 'Streaming error');
              }
            } catch (parseError) {
              // Ignore parse errors for incomplete messages
            }
          }
        }
      };

      // Handle request completion
      xhr.onload = () => {
        if (xhr.status === 200) {
          // Stream completed successfully
          console.log('SSE stream completed');
        } else {
          onError(`HTTP error: ${xhr.status}`);
        }
      };

      // Handle errors
      xhr.onerror = () => {
        onError('Network error during streaming');
      };

      // Send request
      xhr.send(JSON.stringify(request));

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

// Helper function for Base64 encoding (React Native compatible)
function btoa(str: string): string {
  // Use base-64 package which is React Native compatible
  const { encode } = require('base-64');
  return encode(str);
}
