# Scope o alcance

El scope o alcance de una variable es el lugar donde esta puede ser accedida.

<code>
  String variable = "Hola mundo";

if (true) {
String mensaje = "Hola mundo";

}

System.out.println(variable);
System.out.println(mensaje); → Error
</code>

Aquí un listado de ejemplos los cuales nos pueden ayudar a comprender de una mejor manera el switch en Java.

## Estructura básica.

<code>
switch (expression) { 
    case value1:
     // secuencia de sentencias.
     break;
    case value2:
     // secuencia de sentencias.
     break;
    .
    .
    . 
    case valueN :
     // secuencia de sentencias.
     break;
    default:
     // Default secuencia de sentencias.
  }
Ejemplos con tipos de datos enteros.

int i = 2;

switch(i) {
case 0:
System.out.println("i es cero.");
break;
case 1:
System.out.println("i es uno.");
break;
case 2:
System.out.println("i es dos.");
break;
case 3:
System.out.println("i es tres.");
break;
default:
System.out.println("i es mayor a tres.");
}
int i = 2;

switch(i) {
case 0:
case 1:
case 2:
case 3:
case 4:
System.out.println("i es menor que cinco");
break;
case 5:
System.out.println("i es cinco");
break;
case 6:
case 7:
case 8:
case 9:
System.out.println("i es menor que diez y mayor a cinco");
break;
default:
System.out.println("i es diez o mayor a diez");
}
int numeroMes = 4;
String estacion = "", mes = "";

switch (numeroMes) {
case 12:
mes = "Diciembre";
case 1:
mes = "Enero";
case 2:
mes = "Febrero";
estacion = "Invierno";
break;
case 3:
mes = "Marzo";
case 4:
mes = "Abril";
case 5:
mes = "Mayo";
estacion = "Primavera";
break;
case 6:
mes = "Junio";
case 7:
mes = "Julio";
case 8:
mes = "Agosto";
estacion = "Verano";
break;
case 9:
mes = "Septiembre";
case 10:
mes = "Octubre";
case 11:
mes = "Noviembre";
estacion = "Otoño";
break;
}

System.out.println("El mes de " + mes + " se encuentra en la estación " + estacion);
</code>

## Ejemplos con Strings.

Aun que el switch nos permite comparar la expresión con un caso, nosotros debemos de asegurarnos que ambos valores sean iguales; Para ello una buena forma es estandarizar la expresión, ya sea convirtiendo todas sus letras en mayusculas o minúsculas.

<code>
String tipoDia = "";
String diaSemana = "Lunes";

switch (diaSemana.toLowerCase()) {
case "lunes":
tipoDia = "Inicio de semana";
break;
case "martes":
case "míercoles":
case "jueves":
tipoDia = "Mediados de semana";
break;
case "viernes":
tipoDia = "Inicio de fin se semana";
break;
case "sábado":
case "domingo":
tipoDia = "Fin de seman";
break;
}

System.out.println(diaSemana + " es " + tipoDia);
</code>
