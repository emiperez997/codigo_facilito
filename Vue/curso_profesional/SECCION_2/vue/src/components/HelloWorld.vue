<template>
  <button @click="evento">Emit</button>
</template>

<script>
export default {
  props: {
    msg: {
      type: String,
      required: true,
    },
  },

  methods: {
    evento() {
      // console.log("Evento emitido");
      this.$emit("evento", this.msg);
    },
  },
};
</script>
