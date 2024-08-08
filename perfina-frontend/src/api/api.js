// api/api.js
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000',
})

// Set up interceptor once
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export function useApi() {
  return {
    register: (url, credentials, options) => api.post(url, credentials, options),
    login: (url, credentials, options) => api.post(url, credentials, options),
    createInvoice: (url, data, options) => api.post(url, data, options),
  }
}
