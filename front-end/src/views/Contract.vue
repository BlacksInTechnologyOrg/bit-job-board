<template>
  <div class="container">
    <h2>{{ contractdata.title }}</h2>
    <section class="appInfo"><br>
      <div class="postingInfo">
        <p> <b>Location: </b>{{ contractdata.location }}</p>
        <p> <b>Type: </b>{{ contractdata.type }}</p>
        <p> <b>Job Posted: </b>{{ contractdata.publishdate }}</p>
        <p> <b> Contract ID: </b> {{ contractdata.contractid }} </p>
        <p> <b> Author: </b> {{ contractdata.author }} </p>
      </div>
      <h4>Description</h4>
      <p>{{ contractdata.description }}</p>
      {{ contractdata.content }}
    </section>
  </div>
</template>

<script>
import {getContract} from '@/api/api'
export default {
  name: 'Contract',
  data () {
    return {
      contractdata: ''
    }
  },
  created () {
    console.log(this.$route.params.contractid)
    getContract(this.$route.params.contractid).then(response => {
      console.log(response.data)
      this.contractdata = response.data
    })
  }
}
</script>

<style scoped>
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
</style>
