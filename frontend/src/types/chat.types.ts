/**
 * Chat and Message Types
 */

export interface Message {
  id: string;
  conversation_id: string;
  role: 'user' | 'assistant';
  content: string;
  metadata?: {
    usage?: UsageInfo;
    citations?: Citation[];
    [key: string]: any;
  };
  created_at: string;
}

export interface Citation {
  url: string;
  title: string;
  start_index?: number;
  end_index?: number;
}

export interface UsageInfo {
  input_tokens: number;
  output_tokens: number;
  reasoning_tokens?: number;
  total_tokens: number;
}

export interface ChatRequest {
  conversation_id?: string;
  message: string;
  use_web_search?: boolean;
  use_code_interpreter?: boolean;
  reasoning_effort?: 'low' | 'medium' | 'high';
}

export interface ChatResponse {
  message: string;
  conversation_id: string;
  message_id: string;
  usage: UsageInfo;
  citations: Citation[];
  metadata?: Record<string, any>;
}

export interface ChatState {
  currentConversationId: string | null;
  messages: Message[];
  isLoading: boolean;
  isStreaming: boolean;
  streamingText: string;
  error: string | null;
}
