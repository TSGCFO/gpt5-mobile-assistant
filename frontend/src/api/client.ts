/**
 * API Client
 * Axios instance with Basic Authentication interceptors
 */

import axios, { AxiosError, InternalAxiosRequestConfig } from 'axios';
import * as SecureStore from 'expo-secure-store';
import { API_BASE_URL, API_TIMEOUT } from '@/constants/api';

// Create axios instance
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: API_TIMEOUT,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor: Add Basic Auth header
apiClient.interceptors.request.use(
  async (config: InternalAxiosRequestConfig) => {
    try {
      // Get stored credentials from secure storage
      const username = await SecureStore.getItemAsync('username');
      const password = await SecureStore.getItemAsync('password');

      if (username && password) {
        // Create Basic Auth header
        const credentials = `${username}:${password}`;

        // Base64 encode (btoa equivalent for React Native)
        const encodedCredentials = btoa(credentials);

        config.headers.Authorization = `Basic ${encodedCredentials}`;
      }
    } catch (error) {
      console.error('Error retrieving credentials:', error);
    }

    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor: Handle errors
apiClient.interceptors.response.use(
  (response) => response,
  async (error: AxiosError) => {
    // Handle 401 Unauthorized
    if (error.response?.status === 401) {
      // Clear stored credentials
      try {
        await SecureStore.deleteItemAsync('username');
        await SecureStore.deleteItemAsync('password');
      } catch (clearError) {
        console.error('Error clearing credentials:', clearError);
      }

      // Let the application handle redirect to login
      // This will be caught by Redux thunks
    }

    // Handle 429 Rate Limit
    if (error.response?.status === 429) {
      const retryAfter = error.response.headers['retry-after'];
      console.warn(`Rate limited. Retry after ${retryAfter} seconds`);
    }

    // Handle network errors
    if (error.message === 'Network Error') {
      console.error('Network error: Cannot connect to server');
    }

    return Promise.reject(error);
  }
);

export default apiClient;

// Helper function for Base64 encoding (compatible with React Native)
function btoa(str: string): string {
  return Buffer.from(str, 'binary').toString('base64');
}
