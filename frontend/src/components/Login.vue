<template>
<q-page class="window-height window-width row justify-center items-center">
    <div class="column">
      <div class="row">
        <q-card square bordered class="q-pa-lg shadow-1">
          <q-card-section>
            <q-form class="q-gutter-md">
              <q-input square filled clearable v-model="info.username" label="username"/>
              <q-input
                square
                filled
                clearable
                v-model="info.password"
                type="password"
                label="password" />
            </q-form>
          </q-card-section>
          <q-card-actions class="q-px-xs">
            <q-btn
                unelevated
                color="light-green-7"
                size="lg"
                class="full-width"
                label="Login"
                @click="login"
            />
          </q-card-actions>
          <q-card-section class="text-center q-pa-none">
            <a
                href="javascript:"
                class="text-grey-6"
                @click.prevent="register"
            >Created an Account</a>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>
<script>
export default {
  name: 'Login',
  data() {
    return {
      info: {
        username: '',
        password: '',
      },
    };
  },
  methods: {
    login() {
      this.$store.dispatch('StockINFO/loginServer', this.info)
        .then(() => this.$router.push({ path: '/main' }))
        .catch(() => alert('Invalid login'));
    },
    register() {
      this.$router.push({ path: '/register' });
    },
  },
};
</script>
<style scoped>
.q-card {
  width: 360px;
}
</style>
