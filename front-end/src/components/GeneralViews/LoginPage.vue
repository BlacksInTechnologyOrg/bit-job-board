<template>
  <div id="login">
      <alert :message="message"></alert>
      <h1>Login</h1>
      <input type="text" name="username" v-model="input.username" placeholder="Username" />
      <input type="password" name="password" v-model="input.password" placeholder="Password" />
      <button type="button" v-on:click.prevent="login">Login</button>
      <router-link to="/register" class="btn btn-link">Register</router-link>
  </div>
</template>

<script>
  import {logInSite} from '../../api/api'
  import Alert from 'components/UIComponents/Alert.vue'

  export default {
    components: {
      Alert
    },
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
          this.$router.push('/admin/overview')
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
