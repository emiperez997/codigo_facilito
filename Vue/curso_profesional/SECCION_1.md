# SECCION 1

## Ciclo de vida de un componente de Vue

![Ciclo de vida de un componente de Vue](https://es.vuejs.org/images/lifecycle.png)

beforeCreate: Se ejecuta antes de que se cree la instancia de Vue, por lo que no tiene acceso a los datos ni a los métodos del componente.

created: Se ejecuta después de que se haya creado la instancia de Vue, por lo que ya tiene acceso a los datos y métodos del componente. Generalmente se utiliza para hacer peticiones HTTP.

beforeUpdate: Se ejecuta antes de que se actualice el DOM, por lo que no tiene acceso a los datos ni a los métodos del componente.

updated: Se ejecuta después de que se actualice el DOM, por lo que ya tiene acceso a los datos y métodos del componente.

## Directivas

v-model: Enlaza el valor de un input a una variable del componente.
v-bind: Enlaza el valor de un atributo de un elemento HTML a una variable del componente.
v-text: Enlaza el contenido de un elemento HTML a una variable del componente.
v-for: Itera sobre un array y renderiza un elemento HTML por cada elemento del array.

v-if: Renderiza un elemento HTML si se cumple una condición.
v-else: Renderiza un elemento HTML si no se cumple una condición.
v-show: Renderiza un elemento HTML si se cumple una condición, pero lo oculta si no se cumple. Se utiliza cuando un elemento sea muy grande

## Eventos

@click: Se ejecuta cuando se hace click en un elemento HTML.
@copy: Se ejecuta cuando se copia un elemento HTML.

**Modificadores de eventos**

- @click.once: Se ejecuta cuando se hace click en un elemento HTML, pero sólo una vez.
- @click.stop: Evita que el evento se propague a los elementos padre.
- @click.prevent: Evita que se ejecute el comportamiento por defecto del evento.

Estos eventos son parte del DOM y no de Vue, por lo que se pueden utilizar en cualquier framework. Para ver más eventos, puedes consultar la documentación de MDN o W3Schools.

(Eventos)[https://www.w3schools.com/jsref/dom_obj_all.asp]

## Formularios

Metodos:

- submit() → Envía el formulario.
  - @submit.prevent → Evita que se envíe el formulario.

## Class y Style Bindings

:class → Enlaza una clase CSS a un elemento HTML. Se pueden utilizar objetos

## Propiedades computadas

Son metodos cacheables, es decir que se ejecutan una sola vez y se almacenan en memoria.

Las funciones computadas se invocan sin el () al final.

Se declaran con la palabra reservada computed, dentro de nuestro componente.

## Watchers

Se declara con la palabra reservad watch, dentro de nuestro componente.

En nuestro ejemplo, el watcher se ejecuta cada vez que cambia el valor de la propiedad name.

<code>
watch: {
  name(newName, oldName) {
    console.log(newName, oldName);
  }
}
</code>
