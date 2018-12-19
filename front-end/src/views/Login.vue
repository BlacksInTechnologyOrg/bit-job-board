<template>
  <div id="login">
    <alert :message="message"/>
    <h1>Login</h1>
    <input
      v-model="input.username"
      type="text"
      name="username"
      placeholder="Username" >
    <input
      v-model="input.password"
      type="password"
      name="password"
      placeholder="Password" >
    <button
      type="button"
      @click.prevent="login">Login</button>
    <router-link
      to="/register"
      class="btn btn-link">Register</router-link>
  </div>
</template>

<script>
import {logInSite} from '@/api/api'
export default {
  name: 'Login',
  data () {
    return {
      input: {
        username: '',
        password: '',
        jsmessage: '',
        error: ''
      },
      message: '',
      showMessage: false
    }
  },
  methods: {
    login: function () {
      const payload = {
        username: this.input.username,
        password: this.input.password
      }
      logInSite(payload).then(response => {
        console.log('rep')
        this.$router.push('/dashboard')
      })
        .catch(err => {
          console.log('err')
          this.message = err.response.data['message']
          this.showMessage = true
        })
    }
  }
}
</script>

<style scoped>
    #login {
        width: 500px;
        border: 1px solid #CCCCCC;
        background-color: #FFFFFF;
        margin: auto;
        margin-top: 200px;
        padding: 20px;
    }
</style>
