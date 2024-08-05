// api.js
import axios from 'axios'

export function useApi() {
  const api = axios.create({
    baseURL: 'http://localhost:8000',
  })

  return api
}
