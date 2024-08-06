<template>
  <div
    class="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-500 to-purple-600"
  >
    <div class="bg-white p-8 rounded-lg shadow-md w-96">
      <h2 class="text-3xl font-bold mb-6 text-center text-gray-800">Registration</h2>
      <form @submit.prevent="handleSubmit">
        <div class="mb-4">
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <input
            type="email"
            id="email"
            v-model="email"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            required
          />
        </div>
        <div class="mb-6">
          <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
          <input
            type="password"
            id="password"
            v-model="password"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            required
          />
        </div>
        <div class="mb-6">
          <label for="password" class="block text-sm font-medium text-gray-700"
            >Repeat Password</label
          >
          <input
            type="password"
            id="password-repeat"
            v-model="password_repeat"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            required
          />
        </div>
        <button
          :disabled="!isFormValid"
          type="submit"
          class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 transition duration-150 ease-in-out"
        >
          Register
        </button>
      </form>

      <div class="mt-4 text-center">
        <router-link :to="{ name: 'SignIn' }" class="text-sm text-indigo-600 hover:text-indigo-500">
          You already have an account? Sign In
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user_store'

const router = useRouter()

const email = ref('')
const password = ref('')
const password_repeat = ref('')

const error = ref('')

const userStore = useUserStore()

const handleSubmit = async () => {
  if (password.value !== password_repeat.value) {
    error.value = 'Passwords do not match'
    return
  } else {
    const response = await userStore.register({
      username: email.value,
      password: password.value,
    })
    if (response.status == 201 || response.status == 200) {
      clearForm()
      router.push({ name: 'Dashboard' })
    }
  }
}

const clearForm = () => {
  email.value = ''
  password.value = ''
  password_repeat.value = ''
  error.value = ''
}

const isFormValid = computed(() => email.value && password.value && password_repeat.value)
</script>
