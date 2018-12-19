<template>
  <div style="height:100vh">
    <div
      class="cb-intro6"
      style="height:100%;">
      <div class="overlay">
        <v-toolbar
          flat
          color="transparent">
          <v-toolbar-title>BIT Job Board</v-toolbar-title>
          <v-spacer/>
          <v-toolbar-items class="hidden-sm-and-down">
            <v-text-field
              prepend-icon="search"
              single-line
              @keyup.enter="searchln"
            />
          </v-toolbar-items>
          <v-spacer/>
          <v-toolbar-items class="hidden-sm-and-down">
            <v-btn to="/login">Login</v-btn>
            <v-btn to="/login">SIGN UP!</v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <div class="container flex-column d-flex h-100 align-items-start justify-content-center">
          <div class="content">
            <h3>BIT Job Board&nbsp;</h3>
            <p>For Job Seekers and Freelancers</p>
          </div>
          <div class="button">
            <a
              href="#"
              class="btn">Find Out More</a>
            <br>
            <span
              class="fa fa-arrow-right"
              aria-hidden="true"> <b>Build your own</b></span>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      baseUrl: process.env.BASE_URL
    }
  },
  methods: {
    searchln () {
      this.$router.push({name: 'Search', params: { search: 'matt' }})
    }
  }

}
</script>

<style scoped>
  /* intro6 */
  .cb-intro6 {
      width: 100%;
      height: 100vh;
      background-attachment: scroll;
      -webkit-background-size: cover;
      -moz-background-size: cover;
      background-size: cover;
      -o-background-size: cover;
      background-repeat: no-repeat;
      background-position: center center;
      background-image:url(../static/img/landing.jpg);
      background-size:100% 100%;

  }

  .cb-intro6 .overlay {
      background-color: rgba(0, 0, 0, 0.32);
      width: 100%;
      height: 100%;
  }

  .cb-intro6 .content {
      width: 30%;
      position: relative;
  }

  .cb-intro6 .content::before {
      content: "";
      display: block;
      background-color: #fff;
      width: 80px;
      height: 4px;
      position: absolute;
      top: -15px;
  }

  .cb-intro6 .content::after {
      content: "";
      display: block;
      background-color: #fff;
      width: 80px;
      height: 4px;
      position: absolute;
      bottom: -15px;
  }

  .cb-intro6 h3 {
      color: #fff;
      font-size: 42px;
      text-transform: uppercase;
      font-weight: 700;
  }

  .cb-intro6 p {
      font-size: 18px;
      font-weight: 600;
      text-transform: uppercase;
      color: #ffffff;
  }

  .cb-intro6 .rectangle {
      background-color: #f8e71c;
      padding: 3px;
      border: 4px solid #282828;
  }

  .cb-intro6 .button .btn {
      margin-top: 40px;
      text-transform: uppercase;
      border-radius: 40px;
      padding: 12px 24px;
      border: 1px solid #b7b7b7;
      color: #333;
      background-color: #fff;
  }

  .cb-intro6 .button .btn:hover {
      background-color: transparent;
      color: #fff;
  }

  .cb-intro6 .button span {
      margin-top: 20px;
      color: #fff;
  }

  .navi {
    background-color: transparent !important;
  }

</style>
