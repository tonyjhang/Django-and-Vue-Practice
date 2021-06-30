<template>
  <q-page
    class="window-height window-width row justify-center items-center"
  >
    <div class="column q-pa-lg">
      <div class="row">
        <q-card square class="shadow-24" style="width:300px;height:485px;">
          <q-card-section>
            <q-form class="q-px-sm q-pt-xl q-pb-lg">
              <q-input square clearable v-model="info.email" type="email" label="Email">
                <template v-slot:prepend>
                  <q-icon name="email" />
                </template>
              </q-input>
              <q-input square clearable v-model="info.username" type="username" label="Username">
                <template v-slot:prepend>
                  <q-icon name="person" />
                </template>
              </q-input>
              <q-input square clearable v-model="info.password" type="password" label="Password">
                <template v-slot:prepend>
                  <q-icon name="lock" />
                </template>
              </q-input>
            </q-form>
          </q-card-section>
          <q-card-actions class="q-px-lg">
            <q-btn
                unelevated
                size="lg"
                color="light-green-7"
                class="full-width text-white"
                label="Register"
                @click="register"
            />
          </q-card-actions>
          <q-card-section class="text-center q-pa-sm">
            <a
                href="javascript:"
                class="text-grey-6"
                @click.prevent="cancel"
            >Back to login page</a>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>
<script>
export default {
  data() {
    return {
      info: {
        username: '',
        password: '',
        email: '',
      },
    };
  },
  methods: {
    register() {
      this.$store.dispatch('StockINFO/register', this.info)
        .then(() => this.$router.push({ path: '/' }))
        .catch((err) => alert(err.response.data.username));
    },
    cancel() {
      this.$router.push({ path: '/' });
    },
  },
};
</script>
