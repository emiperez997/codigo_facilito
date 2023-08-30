<template>
  <button>
    <slot></slot>
  </button>
</template>

<script>
export default {
  props: ["msg"],
};
</script>
