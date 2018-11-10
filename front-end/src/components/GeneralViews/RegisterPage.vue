<template>
  <div id="register">
      <h1>Login</h1>
      <alert :message="message"></alert>
      <input type="text" name="username" v-model="input.username" placeholder="Username" />
      <input type="password" name="password" v-model="input.password" placeholder="Password" />
      <input type="password" name="confirmpassword" v-model="input.confirmpassword" placeholder="Confirm Password" />
      <input type="text" name="firstname" v-model="input.firstname" placeholder="First Name" />
      <input type="text" name="lastname" v-model="input.lastname" placeholder="Last Name" />
      <input type="email" name="email" v-model="input.email" placeholder="Email" />
      <button type="button" v-on:click.prevent="register">Register</button>
      <router-link to="/" class="btn btn-link">Cancel</router-link>
  </div>
</template>

<script>
  import {registerToSite} from '../../api/api'
  import Alert from 'components/UIComponents/Alert.vue'

  export default {
    name: 'Register',
    components: {
      Alert
    },
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
