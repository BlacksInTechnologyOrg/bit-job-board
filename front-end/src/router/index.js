import Vue from 'vue'
import VueRouter from 'vue-router'
import Navigation from '@/components/private/Navigation'
import Dashboard from '@/components/private/Dashboard'


Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/',
      redirect: { name: 'Dashboard' },
      name: 'Navigation',
      component: Navigation,
      children: [
        {
          path: 'dashboard',
          name: 'Dashboard',
          component: Dashboard
        }
      ]
    },
  ]
})