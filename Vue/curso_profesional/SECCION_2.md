# SECCION 2

## Componentes

**Componente**: Es una instancia de Vue reutilizable

<code>
const component = {
  template: '',
  data() {
    return {
      ...
    }
  },
}
</code>

**Vite**: Es un bundler que permite trabajar con Vue 3. Nos permite desarrollo web con un template de Vue.

- props: Sirve para pasar parametros. Se define dentro del export default de nuestro componente. Se puede insertar un objeto con el tipo de dato y si es requerido o no.

<code>
props: {
  title: {
    type: String,
    required: true,
  },
}
</code>

**Slots**: Nos sirve reemplazar o agregar elementos HTML desde el exterior a un componente.

<code>
<slot></slot> → Le indicamos que el contenido que se encuentre dentro de este slot se va a renderizar en el componente.
</code>

El contenido del slot es lo que se pasa dentro de la declaración del componente
<code>
<Button>Click me</Button> → En este caso seria el texto "Click me"
</code>

Se el puede asignar un nombre y luego llamarlo en el componente con v-slot y luego el nombre

**Emits**: Nos permite emitir eventos desde un componente hijo hacia un componente padre.

this.$emit('nombreEvento', data) → Se emite el evento con el nombre y la data que se quiera enviar.

**Componentes dinámicos**: Son los que cambian de acuerdo a una condición.

- keep-alive: Nos permite mantener el estado de un componente cuando cambiamos de ruta.
