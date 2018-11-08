<template>
    <div id="login">
        <h1>Login</h1>
        <input type="text" name="username" v-model="input.username" placeholder="Username" />
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
        <button type="button" v-on:click.prevent="login">Login</button>
    </div>
</template>

<script>
    import {logInSite} from '../../api/api'

    export default {
      name: 'Login',
      data () {
        return {
          input: {
            username: '',
            password: ''
          }
        }
      },
      methods: {
        login: function () {
          const payload = {
            username: this.input.username,
            password: this.input.password
          }
          logInSite(payload)
          this.$router.push('/admin/overview')
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
