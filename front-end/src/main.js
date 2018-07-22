import '@babel/polyfill'
import Vue from 'vue'
import './plugins/vuetify'
import App from './App'
import router from './router'
import store from './store'

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  store,
  render (h) { return h(App) }
})
