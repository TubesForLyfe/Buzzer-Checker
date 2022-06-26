<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <Probability/>
  </div>
</template>

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
