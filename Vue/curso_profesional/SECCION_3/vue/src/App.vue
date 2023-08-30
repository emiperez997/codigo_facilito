<template>
  <Fade>
    <component :is="currentComponent"></component>
  </Fade>

  <button @click="currentComponent = 'home'">Home</button>
  <button @click="currentComponent = 'about'">About</button>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import Button from "./components/Button.vue";
import AppLayout from "./components/AppLayout.vue";
import Home from "./components/Home.vue";
import About from "./components/About.vue";

import Fade from "./transition/Fade.vue";

export default {
  name: "App",
  data() {
    return {
      // message: "Holis",
      currentComponent: "home",
    };
  },
  components: {
    HelloWorld,
    Button,
    AppLayout,
    Home,
    About,
    Fade,
    Fade,
  },

  methods: {
    handleEvento(value) {
      console.log(value);
    },
  },
};
</script>

<style>
button {
  background-color: #f00;
  color: #fff;
  padding: 10px;
  border-radius: 5px;
  border: none;
  margin: 10px;
}

/* .fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
} */
</style>
