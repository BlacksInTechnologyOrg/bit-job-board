<template>
  <div class="container">
    <h2>{{ jobdata.title }}</h2>
    <section class="appInfo"><br>
      <div class="postingInfo">
        <p> <b>Location: </b>{{ jobdata.location }}</p>
        <p> <b>Type: </b>{{ jobdata.type }}</p>
        <p> <b>Job Posted: </b>{{ jobdata.publishdate }}</p>
        <p> <b> Contract ID: </b> {{ jobdata.jobid }} </p>
        <p> <b> Author: </b> {{ jobdata.author }} </p>
      </div>
      <h4>Description</h4>
      <p>{{ jobdata.description }}</p>
      {{ jobdata.content }}
    </section>
  </div>
</template>

<script>
import {getJob} from '@/api/api'
export default {
  name: 'Job',
  data () {
    return {
      jobdata: ''
    }
  },
  created () {
    getJob(this.$route.params.jobid).then(response => {
      this.jobdata = response.data
    })
  }
}
</script>

<style scoped>
</style>
