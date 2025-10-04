// https://docs.expo.dev/guides/using-eslint/
const { defineConfig } = require('eslint/config');
const expoConfig = require('eslint-config-expo/flat');

module.exports = defineConfig(
  {
    ignores: [
      'node_modules/',
      '.expo/',
      '.expo-shared/',
      'dist/',
      'build/',
      'web-build/',
      'android/',
      'ios/',
      'coverage/',
    ],
  },
  ...expoConfig,
  {
    files: ['metro.config.js', 'babel.config.js'],
    languageOptions: {
      globals: {
        __dirname: 'readonly',
        module: 'readonly',
        require: 'readonly',
      },
    },
  }
);
