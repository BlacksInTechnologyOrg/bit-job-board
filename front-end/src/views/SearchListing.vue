<template>
  <v-container>
    <v-radio-group
      v-model="picked"
      row>
      <v-radio
        label="Jobs"
        value="Jobs"/>
      <v-radio
        label="Contracts"
        value="Contracts"/>
    </v-radio-group>
    <v-layout row>
      <v-flex sm6>
        <v-text-field
          v-model="querydubin"
          label="Solo"
          prepend-icon="search"
          single-line
          solo
          @keyup.enter="searchquery"/>
      </v-flex>
    </v-layout>
    <v-layout
      v-if="searchdata"
      class="mb20">
      <h1>Search Results</h1>
      <v-spacer/>
      <h2 class="lead"><strong class="text-danger">{{ searchdata.length }}</strong> results were found for the search for <strong class="text-danger">{{ querydubin }}</strong></h2>
    </v-layout>

    <section class="col-xs-12 col-sm-6 col-md-12">
      <article
        v-if="this.$route.params.search"
        class="search-result row">
        <div
          v-for="s in searchdata"
          :key="s"
          class="col-xs-12 col-sm-12 col-md-12 excerpet">
          <h3><router-link :to="{ name: 'job', params: { jobid: s.jobid }}">{{ s.title }}</router-link></h3>
          <p>{{ s.description }}</p>
        </div>
        <span class="clearfix borda"/>
      </article>

      <article
        v-if="picked === 'Jobs'"
        class="search-result row">
        <p>{{ searchdata }}</p>
        <div
          v-for="s in searchdata"
          :key="s"
          class="col-xs-12 col-sm-12 col-md-12 excerpet">
          <h3><router-link :to="{ name: 'job', params: { jobid: s.jobid }}">{{ s.title }}</router-link></h3>
          <p>{{ s.description }}</p>
        </div>
        <span class="clearfix borda"/>
      </article>
      <article
        v-else-if="picked === 'Contracts'"
        class="search-result row">
        <div
          v-for="s in searchdata"
          :key="s"
          class="col-xs-12 col-sm-12 col-md-12 excerpet">
          <h3><router-link :to="{ name: 'contract', params: { contractid: s.contractid }}">{{ s.title }}</router-link></h3>
          <p>{{ s.description }}</p>
        </div>
        <span class="clearfix borda"/>
      </article>
    </section>
  </v-container>
</template>

<script>
import {searchContracts, searchJobs} from '@/api/api'

export default {
  name: 'SearchListing',
  data () {
    return {
      picked: 'Jobs',
      searchdata: '',
      querydubin: ''
    }
  },
  created: function () {
    if (this.$route.params.search) {
      searchJobs(this.$route.params.search).then(response => {
        this.searchdata = response.data
      })
    }
  },
  methods: {
    searchquery () {
      if (this.picked === 'Jobs') {
        searchJobs(this.querydubin).then(response => {
          this.searchdata = response.data
        })
      } else if (this.picked === 'Contracts') {
        searchContracts(this.querydubin).then(response => {
          this.searchdata = response.data
        })
      }
    }
  }

}
</script>

<style scoped>
  @import "http://fonts.googleapis.com/css?family=Roboto:300,400,500,700";

.container { margin-top: 20px; }
.mb20 { margin-bottom: 20px; }

.mb20 { padding-left: 15px; border-bottom: 1px solid #ccc; }
.mb20 h1 { font: 500 normal 1.625em "Roboto",Arial,Verdana,sans-serif; color: #2a3644; margin-top: 0; line-height: 1.15; }
.mb20 h2.lead { font: normal normal 1.125em "Roboto",Arial,Verdana,sans-serif; color: #2a3644; margin: 0; padding-bottom: 10px; }

.search-result .thumbnail { border-radius: 0 !important; }
.search-result:first-child { margin-top: 0 !important; }
.search-result { margin-top: 20px; }
.search-result .col-md-2 { border-right: 1px dotted #ccc; min-height: 140px; }
.search-result ul { padding-left: 0 !important; list-style: none;  }
.search-result ul li { font: 400 normal .85em "Roboto",Arial,Verdana,sans-serif;  line-height: 30px; }
.search-result ul li i { padding-right: 5px; }
.search-result .col-md-7 { position: relative; }
.search-result h3 { font: 500 normal 1.375em "Roboto",Arial,Verdana,sans-serif; margin-top: 0 !important; margin-bottom: 10px !important; }
.search-result h3 > a, .search-result i { color: #248dc1 !important; }
.search-result p { font: normal normal 1.125em "Roboto",Arial,Verdana,sans-serif; }
.search-result span.plus { position: absolute; right: 0; top: 126px; }
.search-result span.plus a { background-color: #248dc1; padding: 5px 5px 3px 5px; }
.search-result span.plus a:hover { background-color: #414141; }
.search-result span.plus a i { color: #fff !important; }
.search-result span.border { display: block; width: 97%; margin: 0 15px; border-bottom: 1px dotted #ccc; }

</style>
