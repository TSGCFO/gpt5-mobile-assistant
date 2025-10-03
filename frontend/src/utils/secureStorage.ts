/**
 * Secure Storage Utility
 * Cross-platform storage that uses SecureStore on native and localStorage on web
 */

import * as SecureStore from 'expo-secure-store';
import { Platform } from 'react-native';

/**
 * Storage abstraction that works across all platforms
 * - Native (iOS/Android): Uses expo-secure-store (encrypted)
 * - Web: Falls back to localStorage (NOT encrypted, but functional)
 */
export const secureStorage = {
  /**
   * Store a value securely
   */
  async setItem(key: string, value: string): Promise<void> {
    if (Platform.OS === 'web') {
      // Web: Use localStorage as fallback
      if (typeof globalThis !== 'undefined' && (globalThis as any).localStorage) {
        (globalThis as any).localStorage.setItem(key, value);
      } else {
        console.warn('localStorage not available on web platform');
      }
    } else {
      // Native: Use SecureStore (encrypted)
      await SecureStore.setItemAsync(key, value);
    }
  },

  /**
   * Retrieve a stored value
   */
  async getItem(key: string): Promise<string | null> {
    if (Platform.OS === 'web') {
      // Web: Use localStorage as fallback
      if (typeof globalThis !== 'undefined' && (globalThis as any).localStorage) {
        return (globalThis as any).localStorage.getItem(key);
      } else {
        console.warn('localStorage not available on web platform');
        return null;
      }
    } else {
      // Native: Use SecureStore
      return await SecureStore.getItemAsync(key);
    }
  },

  /**
   * Delete a stored value
   */
  async deleteItem(key: string): Promise<void> {
    if (Platform.OS === 'web') {
      // Web: Use localStorage as fallback
      if (typeof globalThis !== 'undefined' && (globalThis as any).localStorage) {
        (globalThis as any).localStorage.removeItem(key);
      } else {
        console.warn('localStorage not available on web platform');
      }
    } else {
      // Native: Use SecureStore
      await SecureStore.deleteItemAsync(key);
    }
  },

  /**
   * Check if storage is available
   */
  isAvailable(): boolean {
    if (Platform.OS === 'web') {
      return typeof globalThis !== 'undefined' && !!(globalThis as any).localStorage;
    }
    return true; // SecureStore is always available on native
  },
};
