# SECCION 4

## Propiedades globales

**Propiedades globales**: Son las que se pueden utilizar en cualquier componente.

**Como se declaran**:

<code>
app.config.globalProperties.$nombrePropiedad = 'valor'
</code>

**Directivas personalizadas**: Nos permite crear directivas personalizadas para manipular el DOM.

**Como se declaran**:

<code>
Vue.directive('nombreDirectiva', {
  mounted(el, binding) {
    // Se ejecuta cuando se monta el componente
  },
  updated(el, binding) {
    // Se ejecuta cuando se actualiza el componente
  },
  unmounted(el, binding) {
    // Se ejecuta cuando se desmonta el componente
  },
})
</code>
