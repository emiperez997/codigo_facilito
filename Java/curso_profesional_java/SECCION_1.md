# ¿Qué es Java?

- Simple
- Seguro
- Portable
- Orientado a objetos
- Robusto
- Multihilo
- Arquitectura neutral
- Interpretado
- Alto performance
- Distribuido y Dinámico

## Plataforma

- Java Lenguaje
- Paquetes Java
- Java Runtime Environment (JRE) → Nos permite ejecutar programas Java en cualquier plataforma. JVM: Java Virtual Machine

# Ediciones de Java

Fueron desarrolladas para atacar ceirtos problemas en un entorno particular.

- Java ME: Java Micro Edition
- Java SE: Java Standard Edition
- Java EE: Java Enterprise Edition

## Java SE

La version original de Sun Microsystems, es la plataforma base para el desarrollo de aplicaciones Java. Cuenta con clases para agilizar el proceso de desarrollo.

Clases

- Seguridad
- Red
- Acceso a base de datos
- Interfaces gráficas
- Conexion entre dispositivos
- XML

## Java ME

Es una version reducida de la versión standard de Java. Está enfocada a crear aplicaciones moviles o para dispositivos con recursos limitados.

- Consolas de videojuegos
- Celulares
- TV

## Java EE

Es la edición más grande de Java. Es utilizada para crear aplicaciones cliente-servidor. Es una plataforma robusta y escalable. Es utilizada para crear aplicaciones de gran tamaño. Generalmente se utiliza en empresas.

- JSON
- Emails
- Bases de datos
- Transacciones
- Persistencias

# JDK y JRE

Diferencia: JDK es el kit de desarrollo de Java, JRE es el entorno de ejecución de Java. Al instalar JDK, se instala JRE.

# Java Virtual Machine

Puede ser ejecutado en diferentes maquinas, n cantidad de veces. Es un lenguaje compilado e interpretado. El compilador de Java genera un bytecode que es interpretado por la JVM.

# Hola mundo

<code>

class HolaMundo {

public static void main(String[] args) {
System.out.println("Hola Mundo");
}
}
</code>

## Proceso de compilación

> javac HolaMundo.java → Genera un archivo .class
> java HolaMundo → Ejecuta el archivo .class

En caso de que tenga un archivo java en otra carpeta, es necesario agregar al archivo lo siguiente:
<code>
package <carpeta_nombre>;
</code>

Y a la hora de crear el archivo .class:

> javac <carpeta_nombre>/<archivo_nombre>.java
> java <carpeta_nombre>.<archivo_nombre>

Ejemplo:

> javac com/eduardocode/HelloWorld.java
> java com.eduardocode.HelloWorld

# Comentarios de código

- Comentarios de una linea: //
- Comentarios de varias lineas: /\* \*/
