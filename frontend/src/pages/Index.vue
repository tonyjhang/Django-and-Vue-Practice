<template>
  <div class="">
    <login></login>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import Login from '../components/Login';

export default defineComponent({
  name: 'PageIndex',
  components: { Login },
});
</script>
