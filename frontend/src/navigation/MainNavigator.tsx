/**
 * Main Navigator
 * Navigation stack for authenticated users
 */

import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import { ChatScreen } from '@/screens/chat';
import { ConversationsScreen } from '@/screens/conversations';

export type MainStackParamList = {
  Conversations: undefined;
  Chat: { conversationId?: string };
};

const Stack = createStackNavigator<MainStackParamList>();

export const MainNavigator: React.FC = () => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerShown: false,
      }}
      initialRouteName="Conversations"
    >
      <Stack.Screen name="Conversations" component={ConversationsScreen} />
      <Stack.Screen name="Chat" component={ChatScreen} />
    </Stack.Navigator>
  );
};
