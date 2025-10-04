/**
 * Metro Configuration
 * Metro bundler configuration for React Native
 * https://reactnative.dev/docs/metro
 */

const { getDefaultConfig } = require('expo/metro-config');

/** @type {import('expo/metro-config').MetroConfig} */
const config = getDefaultConfig(__dirname);

module.exports = config;
