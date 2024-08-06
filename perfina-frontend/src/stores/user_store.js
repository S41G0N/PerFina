// stores/user_store.js
import { defineStore } from 'pinia'
import { useApi } from '@/api/api'

export const useUserStore = defineStore('user', {
  state: () => ({
    isRegistered: false,
    user: null,
  }),
  getters: {
    isLoggedIn() {
      return this.isRegistered
    },
  },
  actions: {
    checkUserStatus() {
      const token = localStorage.getItem('token')
      this.isRegistered = !!token
      console.log(`User status checked. Is registered: ${this.isRegistered}`)
    },
    async logout() {
      try {
        localStorage.removeItem('token')
        this.isRegistered = false
        this.user = null
        console.log('User logged out successfully')
      } catch (error) {
        console.error('Error during logout:', error)
      }
    },
    async login(credentials) {
      const api = useApi()
      const params = new URLSearchParams()
      params.append('username', credentials.username)
      params.append('password', credentials.password)
      try {
        console.log('Attempting login...')
        const response = await api.login('/token', params, {
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        })
        if (response.status === 200) {
          localStorage.setItem('token', response.data.access_token)
          this.isRegistered = true
          this.user = { username: credentials.username }
          console.log('Login successful')
          return response
        } else {
          console.warn(`Unexpected response status: ${response.status}`)
        }
      } catch (error) {
        console.error('Login failed:', error.message || error)
        throw error
      }
    },
    async register(credentials) {
      const api = useApi()
      try {
        console.log('Attempting registration...')
        const response = await api.register(
          '/register',
          JSON.stringify({
            username: credentials.username,
            password: credentials.password,
          }),
          {
            headers: { 'Content-Type': 'application/json' },
          }
        )
        if (response.status === 200 || response.status === 201) {
          console.log('Registration successful, attempting login...')
          await this.login(credentials)
        } else {
          console.warn(`Unexpected response status: ${response.status}`)
        }
        return response
      } catch (error) {
        console.error('Registration failed:', error.message || error)
        throw error
      }
    },
  },
})

