/**
 * Conversation Slice
 * Manages conversation history and metadata
 */

import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';
import { conversationApi } from '@/api/conversation';
import { ConversationState, Conversation } from '@/types/conversation.types';

const initialState: ConversationState = {
  conversations: [],
  selectedConversation: null,
  isLoading: false,
  error: null,
  total: 0,
};

// Async thunks
export const fetchConversations = createAsyncThunk(
  'conversation/fetchAll',
  async ({ limit = 50, offset = 0 }: { limit?: number; offset?: number }, { rejectWithValue }) => {
    try {
      const response = await conversationApi.getConversations(limit, offset);
      return response;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to fetch conversations');
    }
  }
);

export const fetchConversationDetails = createAsyncThunk(
  'conversation/fetchDetails',
  async (conversationId: string, { rejectWithValue }) => {
    try {
      const conversation = await conversationApi.getConversation(conversationId, true);
      return conversation;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to fetch conversation');
    }
  }
);

export const createConversation = createAsyncThunk(
  'conversation/create',
  async ({ title }: { title?: string } = {}, { rejectWithValue }) => {
    try {
      const conversation = await conversationApi.createConversation(title);
      return conversation;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to create conversation');
    }
  }
);

export const deleteConversation = createAsyncThunk(
  'conversation/delete',
  async (conversationId: string, { rejectWithValue }) => {
    try {
      await conversationApi.deleteConversation(conversationId);
      return conversationId;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to delete conversation');
    }
  }
);

// Slice
const conversationSlice = createSlice({
  name: 'conversation',
  initialState,
  reducers: {
    selectConversation: (state, action: PayloadAction<Conversation | null>) => {
      state.selectedConversation = action.payload;
    },
    clearConversations: (state) => {
      state.conversations = [];
      state.selectedConversation = null;
      state.total = 0;
      state.error = null;
    },
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    // Fetch conversations
    builder
      .addCase(fetchConversations.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(fetchConversations.fulfilled, (state, action) => {
        state.isLoading = false;
        state.conversations = action.payload.conversations;
        state.total = action.payload.total;
      })
      .addCase(fetchConversations.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });

    // Fetch conversation details
    builder
      .addCase(fetchConversationDetails.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(fetchConversationDetails.fulfilled, (state, action) => {
        state.isLoading = false;
        state.selectedConversation = action.payload;
      })
      .addCase(fetchConversationDetails.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });

    // Create conversation
    builder
      .addCase(createConversation.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(createConversation.fulfilled, (state, action) => {
        state.isLoading = false;
        state.conversations.unshift(action.payload);
        state.total += 1;
      })
      .addCase(createConversation.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });

    // Delete conversation
    builder
      .addCase(deleteConversation.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(deleteConversation.fulfilled, (state, action) => {
        state.isLoading = false;
        state.conversations = state.conversations.filter(
          (conv) => conv.id !== action.payload
        );
        state.total -= 1;
        if (state.selectedConversation?.id === action.payload) {
          state.selectedConversation = null;
        }
      })
      .addCase(deleteConversation.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });
  },
});

export const { selectConversation, clearConversations, clearError } = conversationSlice.actions;
export default conversationSlice.reducer;
