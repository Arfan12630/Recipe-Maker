import { createRouter, createWebHistory } from 'vue-router'

import TheHome from '../views/TheHome'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: TheHome
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('../views/TheDashboard.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/TheAbout.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router