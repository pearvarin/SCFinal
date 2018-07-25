import Vue from 'vue'
import Router from 'vue-router'
import Game from '@/components/Game'
import UserAuth from '@/components/UserAuth'
import GameAuth from '@/components/GameAuth'
import GeneralManager from '@/components/GeneralManagerFront'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/game/:uri?',
      name: 'Game',
      component: Game
    },

    {
      path: '/gameauth',
      name: 'GameAuth',
      component: GameAuth
    },

    {
      path: '/auth',
      name: 'UserAuth',
      component: UserAuth
    },

    {
      path: '/general-manager',
      name: 'GeneralManager',
      component: GeneralManager
    },

  ]
})

router.beforeEach((to, from, next) => {
  if (sessionStorage.getItem('authToken') !== null || to.path === '/auth') {
    next()
  } else {
    next('/auth')
  }
})

export default router