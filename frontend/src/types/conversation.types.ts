/**
 * Conversation Types
 */

import { Message } from './chat.types';

export interface Conversation {
  id: string;
  user_id: string;
  title: string | null;
  created_at: string;
  updated_at?: string;
  message_count?: number;
  messages?: Message[];
}

export interface ConversationState {
  conversations: Conversation[];
  selectedConversation: Conversation | null;
  isLoading: boolean;
  error: string | null;
  total: number;
}
