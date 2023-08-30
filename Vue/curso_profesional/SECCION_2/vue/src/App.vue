<template>
  <!-- Componente Padre -->
  <!-- <AppLayout>
    <template v-slot:header>
      <h1>Titulo</h1>
    </template>
    <template v-slot:body>
       Componentes hijos
      <HelloWorld msg="Hola we" @evento="handleEvento" />
      <Button>Enviar </Button>
      <Button>Enviar 2</Button>
    </template>
  </AppLayout> -->

  <keep-alive>
    <component :is="currentComponent"></component>
  </keep-alive>

  <button @click="currentComponent = 'home'">Home</button>
  <button @click="currentComponent = 'about'">About</button>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import Button from "./components/Button.vue";
import AppLayout from "./components/AppLayout.vue";
import Home from "./components/Home.vue";
import About from "./components/About.vue";

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
  },

  methods: {
    handleEvento(value) {
      console.log(value);
    },
  },
};
</script>
