# Tipos de datos

Al ser un lenguaje fuermente tipado, no podemos asignar un valor de un tipo

Tipo de datos

- byte
- short
- int
- long
- char
- float
- double
- boolean

Podemos separarlos en 4 categorias

- Enteros
- Flotantes
- Caracteres
- Booleanos

Enteros

- byte
- short
- int
- long

Flotantes

- float
- double

Caracteres

- char

Booleanos

- boolean

# Palabras reservadas en Java

- abstract continue for new switch
- assert default goto package synchronized
- boolean do if private this
- break double implements protected throw
- byte else import public thows
- case enum instanceof return transient
- catch extends int short try
- char final interface static void
- class finally long strictfp volatile
- const float native super while
  Algo importante a tener en cuenta es que las palabras reservadas no pueden ser utilizadas como nombres de variables, clases o métodos.

> Aunque const y goto son palabras reservadas, estas no son utilizadas en la actualidad.

En adición a este listados podemos agregar true, false y null.

# Métodos print y println

Para que nosotros podamos mostrar un mensaje en consola debemos hacer uso de los métodos print, println o printf. Para este post nos concentramos en print y println, de printf ya estaremos hablando más adelante.

Con el método println el mensaje se imprimirá en consola con un salto de línea.

<code>
System.out.println("Hola Mundo");
System.out.println("Mi nombre es Codi");
</code>

Salida

Hola Mundo
Mi nombre es Codi
Por otro lado, el método print imprimirá el mensaje en la misma línea.

<code>
System.out.print("Hola Mundo");
System.out.print("Mi nombre es Codi");
</code>

Salida

Hola MundoMi nombre es Codi

## Secuencias de escapes

Java nos provee de una secuencia de escapes que nos permiten dar formato a las cadenas de texto con las que nos encontramos trabajando.

\n. Salto de línea.
\t. Tabulador.
\\. Diagonal inversa.
\". Comillas dobles.
\'. Comillas simples.
Estas secuencias pueden ser utilizadas junto con los métodos previamente mencionados.

Ejemplos

<code>
System.out.print("Hola,\nagregamos un salto");
System.out.print("\tagregamos un tab");
System.out.println("");

System.out.println("Mensaje con \\ diagonal inversa");
System.out.println("Mensaje con \" comillas dobles");
System.out.println("Mensaje con \` comillas simples");
</code>

Salida
<code>
Hola,
agregamos un salto agregamos un tab
Mensaje con \ diagonal inversa
Mensaje con " comillas dobles
Mensaje con ' comillas simples

</code>
