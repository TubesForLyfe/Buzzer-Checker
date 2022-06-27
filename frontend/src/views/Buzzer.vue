<template>
  <div class="home">
    <h2>Buzzer Checker</h2>
    <h4>by TubesForLyfe</h4>
    <img alt="Vue logo" src="https://cdn.pixabay.com/photo/2016/11/01/12/09/twitter-logo-1788039_960_720.jpg" class="img">
    <Probability/>
  </div>
</template>

<style>
.img {
  width: 25%;
  height: 25%
}
</style>

<script>
// @ is an alias to /src
import Probability from '@/components/Probability.vue'

export default {
  name: 'BuzzerView',
  components: {
    Probability
  }
}
</script>
