# Listado de ejemplos sobre el método format de la clase String.

Recordemos que el método format retornar un nuevo String. Si nosotros únicamente mostraremos en consola el nuevo String podemos optar por usar el método printf

<code>
System.out.printf(formato, valores);
</code>

## String

<code>
String nombre = "Codi";
String apellido = "Facilito";

String nombreCompleto = String.format("%s %s", nombre, apellido);
System.out.println(nombreCompleto);
</code>

## Enteros

<code>
String resultado = String.format("%d - %d - %d", 10, 20, 30);
System.out.println(resultado);
</code>

## Float

<code>
float pi = 3.14159265359f;

String resultado = String.format("%f - Decimales: %.2f", pi, pi);
System.out.println(resultado);
</code>

## Boolean

<code>
int cantidad = 10;
boolean mayor = cantidad > 5;

String resultado = String.format("La cantidad es mayor a %d : %b",
cantidad, mayor);
System.out.println(resultado);
</code>

## Orden

El reemplazo de los valores es lineal, sin embargo, habrá ocasiones en las cuales nosotros necesitemos especificar el orden, en esos casos seguiremos la siguiente estructura %, posición, $, tipo

<code>
String uno = "Uno";
String dos = "Dos";
String tres = "Tres";

String resultado = String.format("%3$s - %2$s - %1$s",
uno, dos, tres);
System.out.println(resultado);
float pi = 3.14159265359f;

String resultado = String.format("%1f - Decimales: %1$.2f", pi, pi);
System.out.println(resultado);
</code>
