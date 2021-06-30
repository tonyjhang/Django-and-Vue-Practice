<template lang="">
    <div id="chart">
        <apexchart type="bar" height="440" :options="chartOptions" :series="series"></apexchart>
      </div>
</template>
<script>

export default {
  // it for Apexchart get undefind row will raise error,need to fix
  watch: {
    '$store.state.StockINFO.TraceAmout': {
      handler: function () {
        this.series = [];
        let result = [
          { name: 'buy', data: [] },
          { name: 'sell', data: [] },
        ];
        let Amout = this.$store.state.StockINFO.TraceAmout;
        Amout.forEach((amout) => {
          if (amout >= 0) {
            result[0].data.push(amout);
          } else {
            result[1].data.push(amout);
          }
        });
        this.series = result;
      },
    },
  },
  data() {
    return {
      series: [],
      chartOptions: {
        chart: {
          type: 'bar',
          height: 440,
          stacked: true,
        },
        colors: ['#008FFB', '#FF4560'],
        plotOptions: {
          bar: {
            horizontal: true,
            barHeight: '80%',
          },
        },
        dataLabels: {
          enabled: true,
        },
        stroke: {
          width: 1,
          colors: ['#fff'],
        },
        grid: {
          xaxis: {
            lines: {
              show: false,
            },
          },
        },
      },
    };
  },
};
</script>
<style scoped>
</style>
