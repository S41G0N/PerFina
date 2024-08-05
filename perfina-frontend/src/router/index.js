import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import DashboardView from '@/views/DashboardView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: MainView,
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: DashboardView,
    },
    {
      path: '/signin',
      name: 'SignIn',
      component: DashboardView,
    },
  ],
})

export default router
