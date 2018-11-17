<template>
  <div class="container">
    <h2>{{jobdata.title}}</h2>
    <section class="appInfo"><br/>
      <div class="postingInfo">
        <p> <b>Location: </b>{{jobdata.location}}</p>
        <p> <b>Type: </b>{{jobdata.type}}</p>
        <p> <b>Job Posted: </b>{{jobdata.publishdate}}</p>
        <p> <b> Contract ID: </b> {{jobdata.jobid}} </p>
        <p> <b> Author: </b> {{jobdata.author}} </p>
      </div>
      <h4>Description</h4>
      <p>{{jobdata.description}}</p>
      {{jobdata.content}}
    </section>
  </div>
</template>

<script>
  import NavBar from 'components/UIComponents/NavBar.vue'
  import {getJob} from '../../api/api'
  export default {
    name: 'Job',
    component: {
      NavBar
    },
    created () {
      getJob(this.$route.params.jobid).then(response => {
        this.jobdata = response.data
      })
    },
    data () {
      return {
        jobdata: ''
      }
    }
  }
</script>

<style scoped>
  html, body {
  margin: 0;
  padding: 0;
  font-family: arial;
}

#app {
  width: 968px;
  margin: 0 auto;
  margin-top: 50px;
}

.appHeading {
  background-color: #3F96DA;
  padding: 15px;
  margin: 0;
  color: #fff;
  position: relative;
}
.appHeading > * {
  display: inline;
  vertical-align: middle;
}
.appHeading button {
  border: none;
  box-shadow: none;
  background-color: #3278AE;
  font-weight: bold;
  color: #fff;
  padding: 10px;
  border-radius: 2px;
  position: absolute;
  right: 5%;
  top: 12px;
}
.appHeading button:hover {
  background-color: #fff;
  color: #3278AE;
}

.appInfo {
  padding: 15px;
}
.appInfo h4 {
  margin-top: 40px;
  margin-bottom: -5px;
}
.appInfo p {
  line-height: 20px;
}

.postingInfo {
  line-height: 15px;
  font-size: 0.9em;
}

ul {
  line-height: 25px;
}

@media (max-width: 968px) {
  main {
    width: 100%;
    margin-top: 0px;
  }
}
@media (max-width: 548px) {
  .appHeading {
    text-align: center;
  }
  .appHeading > * {
    display: block;
  }
  .appHeading button {
    position: relative;
    right: auto;
    top: auto;
    margin: 0 auto;
  }
}
a {
  text-decoration: none !important;
  color: #fff;
}


</style>
