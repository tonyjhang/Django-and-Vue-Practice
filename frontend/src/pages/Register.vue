<template>
  <div class="">
    <register></register>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import Register from '../components/Register';

export default defineComponent({
  name: 'PageIndex',
  components: { Register },
});
</script>
