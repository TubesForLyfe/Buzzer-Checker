<template>
  <div class="hello">
    <h2>Buzzer Checker</h2>
    <h4>by TubesForLyfe</h4>
    <p>Input some Twitter username</p>
    <form @submit.prevent="CheckUsername">
      <input type="text" v-model="username" />
      <button>Check</button>
    </form>
    <h2>{{ probability }}</h2>
  </div>
</template>

<script>
import Axios from 'axios'
export default {
  name: 'ProbabilityView',
  data() {
    return {
      username: '',
      probability: ''
    }
  },
  methods: {
    CheckUsername() {
      Axios.post(`${process.env.VUE_APP_BUZZER_API}/check-buzzer`, {
        username: this.username
      }).then(response => {
        this.probability = response.data;
      })
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
