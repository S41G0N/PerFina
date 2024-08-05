<template>
  <NavigationBar />
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'
import NavigationBar from '@/components/NavigationBar.vue'
</script>
