/**
 * Chat Screen
 * Main chat interface with streaming support
 */

import React, { useEffect, useRef, useState } from 'react';
import {
  View,
  FlatList,
  StyleSheet,
  ActivityIndicator,
  Text,
  SafeAreaView,
  TouchableOpacity,
} from 'react-native';
import { MessageBubble, ChatInput } from '@/components/chat';
import { colors, spacing, typography } from '@/theme';
import { useAppDispatch, useAppSelector } from '@/store/hooks';
import {
  sendMessage,
  addMessage,
  setStreaming,
  updateStreamingText,
  loadConversationMessages,
} from '@/store/slices/chatSlice';
import { chatApi } from '@/api/chat';
import { Message } from '@/types/chat.types';

interface ChatScreenProps {
  navigation: any;
  route: any;
}

export const ChatScreen: React.FC<ChatScreenProps> = ({ navigation, route }) => {
  const dispatch = useAppDispatch();
  const { messages, isLoading, isStreaming, streamingText, currentConversationId } =
    useAppSelector((state) => state.chat);

  const flatListRef = useRef<FlatList>(null);
  const [useStreaming, setUseStreaming] = useState(true);

  // Load conversation messages if conversation ID is provided
  useEffect(() => {
    const conversationId = route.params?.conversationId;
    if (conversationId && conversationId !== currentConversationId) {
      dispatch(loadConversationMessages(conversationId));
    }
  }, [route.params?.conversationId]);

  // Scroll to bottom when messages change
  useEffect(() => {
    if (messages.length > 0) {
      setTimeout(() => {
        flatListRef.current?.scrollToEnd({ animated: true });
      }, 100);
    }
  }, [messages.length, streamingText]);

  const handleSendMessage = async (content: string) => {
    // Add user message immediately
    const userMessage: Message = {
      id: `temp-${Date.now()}`,
      conversation_id: currentConversationId || '',
      role: 'user',
      content,
      created_at: new Date().toISOString(),
    };
    dispatch(addMessage(userMessage));

    if (useStreaming) {
      // Use streaming
      dispatch(setStreaming(true));

      let fullResponse = '';

      await chatApi.streamMessage(
        {
          conversation_id: currentConversationId || undefined,
          messages: [{ role: 'user', content }],
          use_web_search: true,
          use_code_interpreter: true,
          reasoning_effort: 'medium',
        },
        (textDelta) => {
          fullResponse += textDelta;
          dispatch(updateStreamingText(fullResponse));
        },
        () => {
          // On complete
          const assistantMessage: Message = {
            id: `msg-${Date.now()}`,
            conversation_id: currentConversationId || '',
            role: 'assistant',
            content: fullResponse,
            created_at: new Date().toISOString(),
          };
          dispatch(addMessage(assistantMessage));
          dispatch(setStreaming(false));
        },
        (error) => {
          // On error
          console.error('Streaming error:', error);
          dispatch(setStreaming(false));
        }
      );
    } else {
      // Use regular completion
      await dispatch(
        sendMessage({
          conversation_id: currentConversationId || undefined,
          message: content,
          use_web_search: true,
          use_code_interpreter: true,
          reasoning_effort: 'medium',
        })
      );
    }
  };

  const handleNewConversation = () => {
    navigation.navigate('Conversations');
  };

  const renderMessage = ({ item }: { item: Message }) => (
    <MessageBubble message={item} />
  );

  const renderStreamingMessage = () => {
    if (!isStreaming || !streamingText) return null;

    return (
      <MessageBubble
        message={{
          id: 'streaming',
          conversation_id: currentConversationId || '',
          role: 'assistant',
          content: streamingText,
          created_at: new Date().toISOString(),
        }}
      />
    );
  };

  const renderHeader = () => (
    <View style={styles.header}>
      <TouchableOpacity
        onPress={handleNewConversation}
        style={styles.headerButton}
      >
        <Text style={styles.headerButtonText}>≡</Text>
      </TouchableOpacity>
      <Text style={styles.headerTitle}>GPT-5 Assistant</Text>
      <View style={styles.headerButton} />
    </View>
  );

  return (
    <SafeAreaView style={styles.container}>
      {renderHeader()}

      <FlatList
        ref={flatListRef}
        data={messages}
        renderItem={renderMessage}
        keyExtractor={(item) => item.id}
        contentContainerStyle={styles.messageList}
        ListEmptyComponent={
          <View style={styles.emptyContainer}>
            <Text style={styles.emptyText}>
              Start a conversation with your AI assistant
            </Text>
          </View>
        }
        ListFooterComponent={renderStreamingMessage()}
      />

      {isLoading && !isStreaming && (
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="small" color={colors.primary} />
          <Text style={styles.loadingText}>Thinking...</Text>
        </View>
      )}

      <ChatInput
        onSend={handleSendMessage}
        disabled={isLoading || isStreaming}
      />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.background,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: colors.border,
  },
  headerButton: {
    width: 40,
    height: 40,
    justifyContent: 'center',
    alignItems: 'center',
  },
  headerButtonText: {
    fontSize: 24,
    color: colors.text,
  },
  headerTitle: {
    fontSize: typography.fontSize.lg,
    fontWeight: typography.fontWeight.semibold,
    color: colors.text,
  },
  messageList: {
    paddingVertical: spacing.md,
  },
  emptyContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: spacing.xl,
    paddingVertical: spacing.xxl,
  },
  emptyText: {
    fontSize: typography.fontSize.md,
    color: colors.textSecondary,
    textAlign: 'center',
  },
  loadingContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: spacing.sm,
  },
  loadingText: {
    marginLeft: spacing.sm,
    fontSize: typography.fontSize.sm,
    color: colors.textSecondary,
  },
});
