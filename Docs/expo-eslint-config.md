# Expo ESLint Configuration Guide

This document provides guidance on configuring ESLint for Expo React Native projects, specifically for SDK 52.

## Overview

ESLint is a JavaScript linter that helps find and fix errors in code. This project uses the official Expo ESLint configuration which is tailored for React Native and Expo environments.

**Important Version Notes:**

- **SDK 52 and below**: Uses legacy ESLint config format (`.eslintrc.js`)
- **SDK 53 and above**: Uses new Flat config format (`eslint.config.js`)

This project uses SDK 52, so we use the **legacy config format**.

## Setup

### Initial Installation

Run the Expo CLI command to install dependencies and generate configuration:

```bash
cd frontend
npx expo lint
```

This command will:

1. Install `eslint` and `eslint-config-expo` if not present
2. Create `.eslintrc.js` at the project root
3. Configure the lint script in package.json

### Manual Installation

If you need to install packages manually:

```bash
npm install --save-dev eslint eslint-config-expo
```

### Configuration File

The generated `.eslintrc.js` extends the official Expo config:

```javascript
// .eslintrc.js
module.exports = {
  extends: 'expo',
};
```

## Usage

### Command Line

```bash
# Lint all files
npm run lint

# Or use expo CLI directly
npx expo lint
```

### VS Code Integration

Install the [ESLint extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) to lint code as you type.

If ESLint is not updating, restart the ESLint server:

1. Open Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
2. Run `ESLint: Restart ESLint Server`

## Environment-Specific Configuration

Expo apps run JavaScript in multiple environments:

- **Node.js environment**: `app.config.js`, `metro.config.js`, `babel.config.js`, `app/+html.tsx`
- **React Native environment**: Standard app files like `app/index.js`

### Node.js Globals (Legacy Config)

For files that need Node.js globals (like `__dirname`), add an `eslint-env` comment at the top:

```javascript
/* eslint-env node */

// Now you can use Node.js globals and modules
const path = require('path');
console.log(__dirname);
```

## Prettier Integration

### Installation

```bash
# macOS/Linux
npx expo install prettier eslint-config-prettier eslint-plugin-prettier --dev

# Windows
npx expo install prettier eslint-config-prettier eslint-plugin-prettier "--" --dev
```

### Configuration

Update `.eslintrc.js` to integrate Prettier:

```javascript
// .eslintrc.js
module.exports = {
  extends: ['expo', 'prettier'],
  plugins: ['prettier'],
  rules: {
    'prettier/prettier': 'error', // or 'warn' for warnings instead of errors
  },
};
```

### Custom Prettier Settings

Create `.prettierrc` in the project root:

```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2
}
```

## Performance Optimization

### .eslintignore

Create `.eslintignore` to exclude directories from linting:

```
node_modules/
.expo/
.expo-shared/
dist/
build/
coverage/
android/
ios/
```

## Troubleshooting

### ESLint Config Not Found

**Error**: `ESLint couldn't find a configuration file`

**Solution**: Run `npx expo lint` to generate the configuration file.

### ESLint is Slow

**Problem**: Large projects can make ESLint slow.

**Solutions**:

1. Add comprehensive `.eslintignore` file
2. Exclude unnecessary directories (node_modules, build artifacts)
3. Only lint source files, not generated or third-party code

### TypeScript Errors

**Problem**: TypeScript-specific linting issues.

**Solution**: The `eslint-config-expo` automatically supports TypeScript. Ensure your `tsconfig.json` is properly configured with `moduleResolution: "bundler"` for SDK 52.

## Related Documentation

- [Official Expo ESLint Guide](https://docs.expo.dev/guides/using-eslint/)
- [ESLint Documentation](https://eslint.org/)
- [eslint-config-expo Source](https://github.com/expo/expo/tree/main/packages/eslint-config-expo)
- [Prettier Documentation](https://prettier.io/docs/en/)

## Project-Specific Notes

### Current Configuration

- **Expo SDK**: 52
- **ESLint Version**: 8.57.0
- **Config Format**: Legacy (`.eslintrc.js`)
- **TypeScript**: Enabled with proper moduleResolution

### Path Aliases

The project uses TypeScript path aliases defined in `tsconfig.json`:

- `@/*` → `src/*`
- `@/components/*` → `src/components/*`
- `@/screens/*` → `src/screens/*`
- etc.

ESLint will automatically understand these aliases through the Expo config.

## Common Rules

The `eslint-config-expo` includes sensible defaults for:

- React and React Native best practices
- React Hooks rules
- Accessibility (a11y) rules
- Import/export validation
- TypeScript-specific rules (when using `.ts`/`.tsx` files)

### Example Common Issues

**React Hook Dependencies**:

```javascript
// Warning: React Hook useEffect has a missing dependency
useEffect(() => {
  doSomething(value);
}, []); // Should include 'value' in dependencies
```

**Unused Variables**:

```javascript
// Warning: 'unused' is assigned a value but never used
const unused = 'test';
```

## Best Practices

1. **Run lint before committing**: Add a pre-commit hook to lint staged files
2. **Fix issues incrementally**: Don't disable rules unless absolutely necessary
3. **Use ESLint comments sparingly**: Prefer fixing the issue over disabling the rule
4. **Keep config minimal**: Let `eslint-config-expo` handle most rules
5. **Update regularly**: Keep ESLint and config packages up to date

## Disabling Rules

Only disable rules when necessary:

```javascript
// Disable for a single line
// eslint-disable-next-line no-console
console.log('Debug info');

// Disable for a file section
/* eslint-disable no-console */
console.log('Debug 1');
console.log('Debug 2');
/* eslint-enable no-console */

// Disable for entire file (use sparingly)
/* eslint-disable no-console */
```
