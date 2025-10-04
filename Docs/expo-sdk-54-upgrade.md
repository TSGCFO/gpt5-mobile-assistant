# Expo SDK 54 Upgrade Guide

This document provides comprehensive guidance for upgrading from Expo SDK 52 to SDK 54, including all breaking changes, new features, and migration steps specific to this GPT-5 Mobile Assistant project.

## Version Overview

| Component | SDK 52 | SDK 54 |
|-----------|--------|--------|
| **Expo SDK** | 52.0.0 | 54.0.0 |
| **React Native** | 0.76 | 0.81 |
| **React** | 18.3.1 | 19.1.0 |
| **React Native Web** | 0.19.13 | 0.21.0 |
| **Node.js (min)** | 20.18.x | 20.19.4 |
| **Xcode (min)** | 16.0+ | 16.1+ (26.0 recommended) |
| **Android compileSdk** | 35 | 36 |
| **Android targetSdk** | 34 | 36 |

## Major Changes in SDK 54

### 1. New Architecture Enabled by Default

**Critical:** SDK 54 enables the React Native New Architecture by default on both iOS and Android.

**What This Means:**

- Better performance and modern React features
- **SDK 54 is the FINAL release supporting Legacy Architecture**
- SDK 55+ will ONLY support New Architecture (no opt-out possible)

**How to Configure:**

Enable explicitly (recommended):

```json
// app.json
{
  "expo": {
    "newArchEnabled": true
  }
}
```

Or disable temporarily (not recommended, will break in SDK 55):

```json
// app.json
{
  "expo": {
    "newArchEnabled": false
  }
}
```

**Compatibility Check:**

- All `expo-*` packages in SDK 54 support New Architecture
- Check third-party libraries: Run `npx expo-doctor@latest`
- ~75% of SDK 53+ projects on EAS Build use New Architecture successfully

### 2. ESLint Flat Config (SDK 53+)

**Breaking Change:** SDK 54 uses ESLint 9.x with the new "Flat Config" format.

**Old (SDK 52):**

- ESLint 8.x
- `.eslintrc.js` (legacy format)
- `eslint-config-expo@^7.x`

**New (SDK 54):**

- ESLint 9.x
- `eslint.config.js` (flat format)
- `eslint-config-expo@~10.x`

**Migration Steps:**

1. Update package.json:

```json
{
  "devDependencies": {
    "eslint": "^9.37.0",
    "eslint-config-expo": "~10.0.0"
  }
}
```

2. Delete `.eslintrc.js`

3. Create `eslint.config.js`:

```javascript
// https://docs.expo.dev/guides/using-eslint/
const { defineConfig } = require('eslint/config');
const expoConfig = require('eslint-config-expo/flat');

module.exports = defineConfig(expoConfig);
```

4. For Node.js environment files (metro.config.js, babel.config.js):

```javascript
// eslint.config.js
const { defineConfig, globalIgnores } = require('eslint/config');
const expoConfig = require('eslint-config-expo/flat');

module.exports = defineConfig(
  globalIgnores,
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
```

### 3. React 19.1.0 Changes

**Major React Upgrade:** SDK 54 includes React 19.1.0 (from 18.3.1 in SDK 52).

**Breaking Changes:**

- `ref` is now a prop (no more `forwardRef` needed in many cases)
- Improved error handling
- Better TypeScript types
- Changes to Suspense behavior

**Impact on This Project:**

- Redux may have behavioral changes (test thoroughly)
- React Navigation updated for React 19 compatibility
- Custom hooks may need updates
- Component lifecycle changes

**Testing Focus:**

- Redux state management
- Navigation flows
- Streaming chat functionality
- Error boundaries

### 4. React Native 0.81 Changes

**Precompiled React Native for iOS:**

- 10x faster clean builds (120s → 10s on M4 Max for RNTester)
- XCFrameworks shipped alongside source
- Automatic in SDK 54 (unless using `use_frameworks!`)

**Android Targets API 36 (Android 16):**

- Edge-to-edge ALWAYS enabled (cannot be disabled)
- `react-native-edge-to-edge` built into React Native
- Update `app.json` for edge-to-edge customization:

```json
{
  "expo": {
    "android": {
      "navigationBar": {
        "enforceContrast": true
      }
    }
  }
}
```

**Predictive Back Gesture (Android):**

- Disabled by default in SDK 54
- Enable with:

```json
{
  "expo": {
    "android": {
      "predictiveBackGestureEnabled": true
    }
  }
}
```

### 5. Expo Autolinking Revamp

**Major Changes:**

- React Native modules installed as transitive dependencies are now autolinked
- Linking based on dependency tree, not node_modules scanning
- Unified behavior across Expo and React Native modules
- Better monorepo and isolated dependency support

**Experimental Feature (Recommended):**

```json
// app.json
{
  "expo": {
    "experiments": {
      "autolinkingModuleResolution": true
    }
  }
}
```

**Opt-out (if issues arise):**

```json
// package.json
{
  "expo": {
    "autolinking": {
      "legacy_shallowReactNativeLinking": true,
      "searchPaths": ["./node_modules"]
    }
  }
}
```

### 6. Expo CLI Improvements

**Import Support (`experimentalImportSupport`):**

- **Now enabled by default** (was experimental in SDK 52)
- Better ESM support
- Supports React Compiler and tree shaking
- Live bindings by default (ECMAScript spec compliance)

**Revert if needed:**

```javascript
// metro.config.js
module.exports = {
  experimentalImportSupport: false,
};
```

**Other CLI Changes:**

- Import stack traces enabled by default
- Unhandled promise rejections now logged as errors
- React Compiler enabled in default template
- React Native owner stacks enabled
- CSS auto-prefixing via `lightningcss`

### 7. Expo Updates & EAS Update

**New Features:**

- `Updates.setUpdateRequestHeadersOverride()` - Runtime header overrides
- `useUpdates()` hook includes `downloadProgress` property
- `Updates.reloadAsync()` accepts `reloadScreenOptions` for custom UI

**Example:**

```typescript
import * as Updates from 'expo-updates';

// Override headers (e.g., employee channel)
Updates.setUpdateRequestHeadersOverride({
  'channel': 'employee-beta'
});

// Track download progress
const { downloadProgress } = Updates.useUpdates();

// Custom reload screen
await Updates.reloadAsync({
  reloadScreenOptions: {
    image: require('./assets/splash.png'),
    fadeDuration: 500,
  },
});
```

## Breaking Changes Specific to This Project

### 1. TypeScript Configuration

**Current State:** ✅ Already compatible

- `moduleResolution: "bundler"` is correct for SDK 54
- TypeScript `~5.9.2` is recommended version

**No action needed.**

### 2. Dependencies Compatibility

**Check these packages:**

| Package | SDK 52 Version | SDK 54 Compatibility | Action Needed |
|---------|----------------|----------------------|---------------|
| `@react-navigation/native` | ^6.1.18 | ✅ Compatible | Verify with React 19 |
| `@react-navigation/stack` | ^6.4.1 | ✅ Compatible | Verify with React 19 |
| `@react-navigation/bottom-tabs` | ^6.6.1 | ✅ Compatible | Verify with React 19 |
| `@reduxjs/toolkit` | ^2.2.7 | ✅ Compatible | Test thoroughly with React 19 |
| `react-redux` | ^9.1.2 | ✅ Compatible | Test thoroughly with React 19 |
| `redux-persist` | ^6.0.0 | ⚠️ Check | May need update for React 19 |
| `expo-secure-store` | ~15.0.7 | ✅ Compatible | Included in SDK 54 |
| `axios` | ^1.7.7 | ✅ Compatible | No changes needed |

**Run Expo Doctor:**

```bash
npx expo-doctor@latest
```

### 3. React Native SafeAreaView (Deprecated)

**This project uses:** `react-native-safe-area-context` ✅

**No action needed** - already using the recommended alternative.

### 4. expo-av (Deprecated, Removed in SDK 55)

**This project:** Does not use `expo-av` ✅

**No action needed.**

### 5. expo-file-system API Change

**This project:** Does not appear to use `expo-file-system` extensively ✅

**If using:** Update imports from `expo-file-system` to `expo-file-system/legacy`, or migrate to new API.

## Deprecations & Removals

### Deprecated in SDK 54 (Removed in SDK 55+)

1. **`expo-build-properties` field `enableProguardInReleaseBuilds`**
   - Use `enableMinifyInReleaseBuilds` instead

2. **`notification` config field in app.json**
   - Use `expo-notifications` config plugin

3. **`expo-av` package**
   - Migrate to `expo-audio` and `expo-video`

4. **Legacy Architecture**
   - SDK 55+ will only support New Architecture

### Removed in SDK 54

1. **First-party JSC support**
   - Only Hermes supported natively
   - Use community JSC if needed: <https://github.com/react-native-community/javascriptcore>

2. **Metro internal imports via `metro/src/..`**
   - Use `metro/private/..` or public APIs

## New Features in SDK 54

### 1. iOS 26 & Liquid Glass Effects

**Liquid Glass Views:**

- New `expo-glass-effect` library
- `<GlassView>` and `<GlassContainer>` components
- Requires Xcode 26 (currently RC, GM Sept 15)

**Icon Composer Support:**

```json
// app.json
{
  "expo": {
    "ios": {
      "icon": "./assets/icon.icon"
    }
  }
}
```

### 2. Expo Router v6

**New Features:**

- Link previews (iOS view controller previews)
- Beta native tabs (iOS/Android)
- Experimental server middleware
- `TextDecoderStream` and `TextEncoderStream` in native runtime

### 3. New Packages

**expo-app-integrity:**

- Verify app integrity (DeviceCheck on iOS, Play Integrity on Android)

**expo-blob:**

- Work with binary large objects (W3C spec compliant)
- Beta release

**expo-maps enhancements:**

- JSON/Google Cloud map ID styling
- POI filtering on Apple Maps

### 4. expo-sqlite Improvements

- `loadExtensionAsync()` and `loadExtensionSync()` APIs
- sqlite-vec extension (vector data processing for RAG AI)
- localStorage web API implementation

### 5. Build Cache Providers (Stable)

**EAS Build Cache Provider:**

```bash
npx expo install eas-build-cache-provider
```

```json
// app.json
{
  "expo": {
    "buildCacheProvider": "eas"
  }
}
```

## Upgrade Steps

### Step 1: Backup and Preparation

```bash
# Commit current changes
git add .
git commit -m "Pre-SDK 54 upgrade checkpoint"

# Create upgrade branch
git checkout -b upgrade/sdk-54
```

### Step 2: Update Dependencies

```bash
cd frontend

# Update Expo and dependencies
npx expo install expo@^54.0.0 --fix

# Install with legacy peer deps (React 19 conflicts)
npm install --legacy-peer-deps
```

### Step 3: Upgrade ESLint

1. Update package.json:

```bash
npm install --save-dev eslint@^9.37.0 eslint-config-expo@~10.0.0 --legacy-peer-deps
```

2. Delete `.eslintrc.js`

3. Create `eslint.config.js` (see ESLint section above)

### Step 4: Update app.json

```json
{
  "expo": {
    "name": "GPT-5 Assistant",
    "slug": "gpt5-assistant",
    "version": "1.0.0",
    "orientation": "portrait",
    "userInterfaceStyle": "automatic",
    "newArchEnabled": true,
    "ios": {
      "supportsTablet": true,
      "bundleIdentifier": "com.gpt5assistant.app"
    },
    "android": {
      "package": "com.gpt5assistant.app",
      "navigationBar": {
        "enforceContrast": true
      }
    },
    "experiments": {
      "autolinkingModuleResolution": true
    },
    "plugins": [
      "expo-secure-store"
    ]
  }
}
```

### Step 5: Run Expo Doctor

```bash
npx expo-doctor@latest
```

Fix any reported issues.

### Step 6: Clean and Rebuild

```bash
# Clear all caches
npx expo start --clear

# Test TypeScript
npx tsc --noEmit

# Run linter
npm run lint

# Test on platforms
npx expo run:android
npx expo run:ios
```

### Step 7: Test Critical Functionality

- [ ] User authentication (login/register)
- [ ] Secure storage (credentials)
- [ ] Chat functionality
- [ ] Streaming responses
- [ ] Redux state management
- [ ] Navigation flows
- [ ] Backend API communication

### Step 8: Update Documentation

Update CLAUDE.md references from SDK 52 to SDK 54.

## Rollback Procedure

If critical issues arise:

```bash
cd frontend

# Revert package.json changes
git checkout HEAD -- package.json

# Revert ESLint config
git checkout HEAD -- eslint.config.js
# Restore .eslintrc.js if deleted

# Revert app.json
git checkout HEAD -- app.json

# Reinstall dependencies
npm install --legacy-peer-deps

# Clear caches
npx expo start --clear
```

## Troubleshooting

### Issue: React 19 Peer Dependency Conflicts

**Solution:** Use `--legacy-peer-deps` flag:

```bash
npm install --legacy-peer-deps
```

### Issue: ESLint Not Finding Config

**Symptoms:** `ESLint couldn't find an eslint.config.(js|mjs|cjs) file`

**Solution:**

1. Ensure `eslint.config.js` exists (not `.eslintrc.js`)
2. Verify ESLint version is 9.x: `npx eslint --version`
3. Check `eslint-config-expo` version is ~10.x

### Issue: New Architecture Build Errors

**Solution:** Temporarily disable New Architecture:

```json
// app.json
{
  "expo": {
    "newArchEnabled": false
  }
}
```

**Note:** This is not a long-term solution (breaks in SDK 55).

### Issue: Metro Bundler Errors

**Solution:**

```bash
# Clear all caches
npx expo start --clear

# If that doesn't work
rm -rf node_modules
npm install --legacy-peer-deps
npx expo start --clear
```

### Issue: Redux Behavior Changes

**Symptoms:** State updates not working as expected

**Solution:**

1. Review React 19 behavioral changes
2. Check Redux DevTools for state transitions
3. Verify `react-redux` is v9.1.2+
4. Test with New Architecture disabled to isolate issue

### Issue: Navigation Crashes

**Symptoms:** App crashes on navigation

**Solution:**

1. Ensure all `@react-navigation/*` packages are updated
2. Check for React 19 incompatibilities in custom navigators
3. Review SafeAreaView usage (should use `react-native-safe-area-context`)

## Additional Resources

- [Official SDK 54 Changelog](https://expo.dev/changelog/sdk-54)
- [React Native 0.81 Release Notes](https://reactnative.dev/blog/2025/08/12/react-native-0.81)
- [React 19.1 Changelog](https://github.com/facebook/react/releases/tag/v19.1.0)
- [Expo SDK 54 API Reference](https://docs.expo.dev/versions/v54.0.0/)
- [New Architecture Migration Guide](https://docs.expo.dev/guides/new-architecture/)
- [Troubleshooting SDK Upgrades](https://expo.fyi/troubleshooting-sdk-upgrades)

## Summary Checklist

Before marking upgrade complete:

- [ ] `expo@^54.0.0` installed
- [ ] ESLint upgraded to 9.x with Flat config
- [ ] app.json updated with New Architecture config
- [ ] Expo Doctor shows no critical issues
- [ ] TypeScript compiles without errors
- [ ] ESLint passes without errors
- [ ] All tests pass
- [ ] Critical user flows tested
- [ ] CLAUDE.md updated
- [ ] Git commit created

## Post-Upgrade Monitoring

Monitor for:

- Redux state management issues
- Navigation crashes or unexpected behavior
- Streaming response failures
- Performance regressions
- Memory leaks

If issues persist beyond 48 hours of active testing, consider rollback and investigation.

---

**Last Updated:** 2025-10-04
**SDK Version:** 54.0.12
**Project:** GPT-5 Mobile Assistant
