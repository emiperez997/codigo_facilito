import { createApp } from "vue";
import App from "./App.vue";
import "./index.css";

const app = createApp(App);

app.config.globalProperties.$filters = {
  toUppercaseLocal(value) {
    return value.toUpperCase();
  },
};

// O
// app.config.globalProperties = {
//   $filters: {
//     toUppercaseLocal(value) {
//       return value.toUpperCase();
//     },
//   },
// };

// Directivas
app.directive("background", {
  beforeMount(el, binding, vnode, prevVnode) {
    el.style.backgroundColor = binding.value;
  },
});

app.mount("#app");
