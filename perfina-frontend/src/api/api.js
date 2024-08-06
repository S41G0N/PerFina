// api.js
import axios from 'axios'

export function useApi() {
  const api = axios.create({
    baseURL: 'http://localhost:8000',
  })

  // Add token to the request if available
  api.interceptors.request.use((config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  })

  return api
}

