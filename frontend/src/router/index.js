import { createRouter, createWebHistory } from 'vue-router'
import Buzzer from '../views/Buzzer.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Buzzer
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
