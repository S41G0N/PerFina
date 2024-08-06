<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Personal Finance Tracker</h1>
  </div>
  <div>
    <button @click="fetchData" :disabled="loading">Refresh Data</button>
    <p v-if="loading">Loading...</p>
    <p v-else-if="error">{{ error }}</p>
    <div v-else-if="data">
      <!-- Display your data here -->
      {{ data }}
    </div>
  </div>
</template>

<script setup>
import { useApi } from '@/api/api'
import { ref, onMounted } from 'vue'
const api = useApi()
const data = ref(null)
const loading = ref(false)
const error = ref(null)

async function fetchData() {
  loading.value = true
  error.value = null
  try {
    const response = await api.get('/transactions/1')
    data.value = response.data
    console.log(data.value)
  } catch (err) {
    error.value = err.message || 'An error occurred'
    console.error('Error fetching data:', err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchData()
})
</script>
