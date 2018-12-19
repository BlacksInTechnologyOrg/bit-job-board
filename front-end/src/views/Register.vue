<template>
  <div id="register">
    <h1>Login</h1>
    <alert :message="message"/>
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
    <input
      v-model="input.confirmpassword"
      type="password"
      name="confirmpassword"
      placeholder="Confirm Password" >
    <input
      v-model="input.firstname"
      type="text"
      name="firstname"
      placeholder="First Name" >
    <input
      v-model="input.lastname"
      type="text"
      name="lastname"
      placeholder="Last Name" >
    <input
      v-model="input.email"
      type="email"
      name="email"
      placeholder="Email" >
    <button
      type="button"
      @click.prevent="register">Register</button>
    <router-link
      to="/login"
      class="btn btn-link">Login</router-link>
  </div>
</template>

<script>
import {registerToSite} from '@/api/api'

export default {
  name: 'Register',
  data () {
    return {
      input: {
        username: '',
        password: '',
        confirmpassword: '',
        firstname: '',
        lastname: '',
        email: '',
        error: ''
      },
      message: '',
      showMessage: false
    }
  },
  methods: {
    register: function () {
      const payload = {
        username: this.input.username,
        password: this.input.password,
        confirmpassword: this.input.confirmpassword,
        firstname: this.input.firstname,
        lastname: this.input.lastname,
        email: this.input.email
      }
      if (this.input.password !== this.input.confirmpassword) {
        this.message = 'Passwords do not match!'
      } else {
        registerToSite(payload).then(response => {
          console.log('rep')
          // this.$router.push('/')
        })
          .catch(error => {
            console.log('err')
            this.message = error.response.data['message']
            this.showMessage = true
          })
      }
    }

  }
}
</script>

<style scoped>
    #register {
        width: 500px;
        border: 1px solid #CCCCCC;
        background-color: #FFFFFF;
        margin: auto;
        margin-top: 200px;
        padding: 20px;
    }
</style>
