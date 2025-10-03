/**
 * API Constants
 */

// Get API base URL from environment variables
// Modern Expo (SDK 50+) uses EXPO_PUBLIC_ prefix for environment variables
export const API_BASE_URL =
  process.env.EXPO_PUBLIC_API_BASE_URL ||
  'http://localhost:8000/api/v1';

// API endpoints
export const API_ENDPOINTS = {
  // Auth
  AUTH_REGISTER: '/auth/register',
  AUTH_VERIFY: '/auth/verify',
  AUTH_ME: '/auth/me',

  // Chat
  CHAT_COMPLETIONS: '/chat/completions',
  CHAT_STREAM: '/chat/stream',

  // Conversations
  CONVERSATIONS: '/chat/conversations',
  CONVERSATION_DETAIL: (id: string) => `/chat/conversations/${id}`,
  CONVERSATION_MESSAGES: (id: string) => `/chat/conversations/${id}/messages`,

  // Health
  HEALTH: '/health',
};

// Request timeout (30 seconds)
export const API_TIMEOUT = 30000;

// Streaming timeout (5 minutes for long responses)
export const STREAMING_TIMEOUT = 300000;
