/**
 * Chat Slice
 * Manages active chat session and messages
 */

import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';
import { chatApi } from '@/api/chat';
import { ChatState, Message, ChatRequest, ChatResponse } from '@/types/chat.types';

const initialState: ChatState = {
  currentConversationId: null,
  messages: [],
  isLoading: false,
  isStreaming: false,
  streamingText: '',
  error: null,
};

// Async thunks
export const sendMessage = createAsyncThunk(
  'chat/sendMessage',
  async (request: ChatRequest, { rejectWithValue }) => {
    try {
      const response = await chatApi.sendMessage(request);
      return response;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to send message');
    }
  }
);

export const loadConversationMessages = createAsyncThunk(
  'chat/loadMessages',
  async (conversationId: string, { rejectWithValue }) => {
    try {
      const messages = await chatApi.getConversationMessages(conversationId);
      return { conversationId, messages };
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to load messages');
    }
  }
);

// Slice
const chatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    setCurrentConversation: (state, action: PayloadAction<string | null>) => {
      state.currentConversationId = action.payload;
      if (!action.payload) {
        state.messages = [];
      }
    },
    addMessage: (state, action: PayloadAction<Message>) => {
      state.messages.push(action.payload);
    },
    updateStreamingText: (state, action: PayloadAction<string>) => {
      state.streamingText = action.payload;
    },
    setStreaming: (state, action: PayloadAction<boolean>) => {
      state.isStreaming = action.payload;
      if (!action.payload) {
        state.streamingText = '';
      }
    },
    clearMessages: (state) => {
      state.messages = [];
      state.currentConversationId = null;
      state.streamingText = '';
      state.error = null;
    },
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    // Send message
    builder
      .addCase(sendMessage.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(sendMessage.fulfilled, (state, action) => {
        state.isLoading = false;
        state.currentConversationId = action.payload.conversation_id;

        // Add assistant message
        const assistantMessage: Message = {
          id: action.payload.message_id,
          conversation_id: action.payload.conversation_id,
          role: 'assistant',
          content: action.payload.message,
          metadata: {
            usage: action.payload.usage,
            citations: action.payload.citations,
          },
          created_at: new Date().toISOString(),
        };
        state.messages.push(assistantMessage);
      })
      .addCase(sendMessage.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });

    // Load messages
    builder
      .addCase(loadConversationMessages.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(loadConversationMessages.fulfilled, (state, action) => {
        state.isLoading = false;
        state.currentConversationId = action.payload.conversationId;
        state.messages = action.payload.messages;
      })
      .addCase(loadConversationMessages.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });
  },
});

export const {
  setCurrentConversation,
  addMessage,
  updateStreamingText,
  setStreaming,
  clearMessages,
  clearError,
} = chatSlice.actions;

export default chatSlice.reducer;
