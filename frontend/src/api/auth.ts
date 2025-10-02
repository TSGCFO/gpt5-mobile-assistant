/**
 * Authentication API
 * User registration and login endpoints
 */

import apiClient from './client';
import * as SecureStore from 'expo-secure-store';
import { API_ENDPOINTS } from '@/constants/api';
import { User, RegisterRequest, LoginRequest } from '@/types/auth.types';

export const authApi = {
  /**
   * Register a new user
   */
  async register(data: RegisterRequest): Promise<User> {
    const response = await apiClient.post<User>(API_ENDPOINTS.AUTH_REGISTER, data);

    // After successful registration, store credentials for auto-login
    await SecureStore.setItemAsync('username', data.username);
    await SecureStore.setItemAsync('password', data.password);

    return response.data;
  },

  /**
   * Login (verify credentials and store them)
   */
  async login(data: LoginRequest): Promise<User> {
    // Create temporary Basic Auth header for this request
    const credentials = btoa(`${data.username}:${data.password}`);

    const response = await apiClient.post<{ message: string; user: User }>(
      API_ENDPOINTS.AUTH_VERIFY,
      {},
      {
        headers: {
          Authorization: `Basic ${credentials}`,
        },
      }
    );

    // If successful, store credentials securely
    await SecureStore.setItemAsync('username', data.username);
    await SecureStore.setItemAsync('password', data.password);

    return response.data.user;
  },

  /**
   * Logout (clear stored credentials)
   */
  async logout(): Promise<void> {
    await SecureStore.deleteItemAsync('username');
    await SecureStore.deleteItemAsync('password');
  },

  /**
   * Check if user is logged in
   */
  async isAuthenticated(): Promise<boolean> {
    try {
      const username = await SecureStore.getItemAsync('username');
      const password = await SecureStore.getItemAsync('password');
      return !!(username && password);
    } catch (error) {
      return false;
    }
  },

  /**
   * Get current user information
   */
  async getCurrentUser(): Promise<User> {
    const response = await apiClient.get<User>(API_ENDPOINTS.AUTH_ME);
    return response.data;
  },
};

// Helper function for Base64 encoding
function btoa(str: string): string {
  return Buffer.from(str, 'binary').toString('base64');
}
