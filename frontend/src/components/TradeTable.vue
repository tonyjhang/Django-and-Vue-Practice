<template>
  <div class="q-pa-md">
    <q-table
      :rows="rows"
      row-key="brokerage_name"
    />
  </div>
</template>
<script>
import { mapGetters } from 'vuex';

export default {
  computed: {
    ...mapGetters({
      rows: 'StockINFO/getDetail',
    }),
  },
};
</script>
