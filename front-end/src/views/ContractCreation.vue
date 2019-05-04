<template>
  <v-form>
    <v-container py-0>
      <v-layout wrap>
        <v-flex
          xs12
          md4
        >
          <v-text-field
            v-model="title"
            label="Title"
          />
        </v-flex>
        <v-flex
          xs12
          md4
        >
          <v-text-field
            v-model="description"
            class="purple-input"
            label="Description"
          />
        </v-flex>
        <v-flex
          xs12
          md4
        >
          <v-text-field
            label="tags"
            class="purple-input"/>
        </v-flex>
        <v-flex xs12>
          <v-textarea
            v-model="content"
            class="purple-input"
            label="Content"
          />
        </v-flex>
        <v-flex
          xs12
          text-xs-right
        >
          <v-btn
            class="mx-0 font-weight-light"
            color="success"
            @click.prevent="create"
          >
            Create
          </v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </v-form>

</template>

<script>
  import {createContract} from '../api/api'

  export default {
    name: 'ContractCreation',
    data () {
      return {
        title: '',
        description: '',
        content: ''
      }
    },
    methods: {
      create() {
        const payload = {
          title: this.title,
          description: this.description,
          content: this.content
        }
        createContract(payload)
      }
    }
  }
</script>

<style scoped>

</style>
