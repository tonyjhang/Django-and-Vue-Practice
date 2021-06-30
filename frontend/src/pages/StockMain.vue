<template>
    <q-page-container>
        <div class="row">
            <div class="col-5">
                <q-select
                    standout="bg-teal text-white"
                    :options="options"
                    label="stock"
                    v-model="info.stockNum"
                />
            </div>
            <div class="col-6">
                <q-input
                    filled
                    v-model="info.date"
                    mask="####-##-##"
                    label="select date"
                >
                    <template v-slot:append>
                        <q-icon name="event" class="cursor-pointer">
                            <q-popup-proxy
                                ref="qDateProxy"
                                transition-show="scale"
                                transition-hide="scale"
                            >
                                <q-date v-model="info.date"
                                    @input="() => $refs.qDateProxy.hide()"
                                ></q-date>
                            </q-popup-proxy>
                        </q-icon>
                    </template>
                </q-input>
            </div>
        <div class="col">
            <q-btn
                color="light-green-7"
                label="search"
                @click="search"
                size="lg"
            />
        </div>
        </div>
        <div class="row">
            <div class="col-4">
                <TradeChart/>
            </div>
            <div class="col-1"/>
            <div class="col-7">
                <TradeTable/>
            </div>
        </div>
    </q-page-container>
</template>
<script>
import { mapGetters } from 'vuex';
import TradeChart from '../components/TradeChart';
import TradeTable from '../components/TradeTable';

export default {
  components: { TradeChart, TradeTable },
  computed: {
    ...mapGetters({
      options: 'StockINFO/getTraceList',
    }),
  },
  data() {
    return {
      info: {
        stockNum: '',
        date: '',
      },
    };
  },
  methods: {
    search() {
      this.$store.dispatch('StockINFO/getDetail', this.info);
    },
  },
};
</script>
<style scoped>
</style>
