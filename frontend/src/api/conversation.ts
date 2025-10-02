/**
 * Conversation API
 * Conversation management endpoints
 */

import apiClient from './client';
import { API_ENDPOINTS } from '@/constants/api';
import { Conversation } from '@/types/conversation.types';

export const conversationApi = {
  /**
   * Get list of conversations
   */
  async getConversations(
    limit = 50,
    offset = 0
  ): Promise<{ conversations: Conversation[]; total: number }> {
    const params = new URLSearchParams({
      limit: limit.toString(),
      offset: offset.toString(),
    });

    const response = await apiClient.get<{
      conversations: Conversation[];
      total: number;
    }>(`${API_ENDPOINTS.CONVERSATIONS}?${params.toString()}`);

    return response.data;
  },

  /**
   * Get a specific conversation
   */
  async getConversation(
    conversationId: string,
    includeMessages = false
  ): Promise<Conversation> {
    const params = new URLSearchParams({
      include_messages: includeMessages.toString(),
    });

    const response = await apiClient.get<Conversation>(
      `${API_ENDPOINTS.CONVERSATION_DETAIL(conversationId)}?${params.toString()}`
    );

    return response.data;
  },

  /**
   * Create a new conversation
   */
  async createConversation(title?: string): Promise<Conversation> {
    const response = await apiClient.post<Conversation>(API_ENDPOINTS.CONVERSATIONS, {
      title,
    });

    return response.data;
  },

  /**
   * Delete a conversation
   */
  async deleteConversation(conversationId: string): Promise<void> {
    await apiClient.delete(API_ENDPOINTS.CONVERSATION_DETAIL(conversationId));
  },
};
