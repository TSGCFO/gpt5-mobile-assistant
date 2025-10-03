/**
 * Button Component
 * Reusable button with different variants
 */

import React from 'react';
import {
  TouchableOpacity,
  Text,
  StyleSheet,
  ActivityIndicator,
  TouchableOpacityProps,
} from 'react-native';
import { colors, spacing, typography } from '@/theme';

interface ButtonProps extends TouchableOpacityProps {
  title: string;
  variant?: 'primary' | 'secondary' | 'outline' | 'text';
  loading?: boolean;
  fullWidth?: boolean;
}

export const Button: React.FC<ButtonProps> = ({
  title,
  variant = 'primary',
  loading = false,
  fullWidth = false,
  disabled,
  style,
  ...props
}) => {
  const getButtonStyle = () => {
    const styles: any = [stylesBase.button];

    if (fullWidth) styles.push(stylesBase.fullWidth);

    switch (variant) {
      case 'primary':
        styles.push(stylesBase.primary);
        break;
      case 'secondary':
        styles.push(stylesBase.secondary);
        break;
      case 'outline':
        styles.push(stylesBase.outline);
        break;
      case 'text':
        styles.push(stylesBase.text);
        break;
    }

    if (disabled) styles.push(stylesBase.disabled);

    return styles;
  };

  const getTextStyle = () => {
    const styles: any = [stylesBase.buttonText];

    switch (variant) {
      case 'primary':
        styles.push(stylesBase.primaryText);
        break;
      case 'secondary':
        styles.push(stylesBase.secondaryText);
        break;
      case 'outline':
        styles.push(stylesBase.outlineText);
        break;
      case 'text':
        styles.push(stylesBase.textVariantText);
        break;
    }

    if (disabled) styles.push(stylesBase.disabledText);

    return styles;
  };

  return (
    <TouchableOpacity
      style={[...getButtonStyle(), style]}
      disabled={disabled || loading}
      {...props}
    >
      {loading ? (
        <ActivityIndicator
          color={variant === 'primary' ? colors.background : colors.primary}
        />
      ) : (
        <Text style={getTextStyle()}>{title}</Text>
      )}
    </TouchableOpacity>
  );
};

const stylesBase = StyleSheet.create({
  button: {
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.lg,
    borderRadius: 12,
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: 50,
  },
  fullWidth: {
    width: '100%',
  },
  primary: {
    backgroundColor: colors.primary,
  },
  secondary: {
    backgroundColor: colors.secondary,
  },
  outline: {
    backgroundColor: 'transparent',
    borderWidth: 2,
    borderColor: colors.primary,
  },
  text: {
    backgroundColor: 'transparent',
  },
  disabled: {
    backgroundColor: colors.disabled,
    opacity: 0.6,
  },
  buttonText: {
    fontSize: typography.fontSize.md,
    fontWeight: typography.fontWeight.semibold,
  },
  primaryText: {
    color: colors.background,
  },
  secondaryText: {
    color: colors.background,
  },
  outlineText: {
    color: colors.primary,
  },
  textVariantText: {
    color: colors.primary,
  },
  disabledText: {
    color: colors.textSecondary,
  },
});
