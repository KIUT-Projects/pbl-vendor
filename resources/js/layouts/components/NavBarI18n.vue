<script setup>
import NavBarI18n from '@core/components/I18n.vue'
import { useThemeConfig } from '@core/composable/useThemeConfig'

const { isAppRtl } = useThemeConfig()

const i18nCompLanguages = [
  {
    label: 'English',
    i18nLang: 'en',
  },
  {
    label: 'Русский',
    i18nLang: 'ru',
  },
  {
    label: 'O`zbekcha',
    i18nLang: 'uz',
  },
  {
    label: 'Узбекча',
    i18nLang: 'oz',
  },
]
</script>

<template>
  <NavBarI18n
    :languages="i18nCompLanguages"
    @change="handleLangChange"
  />
</template>
