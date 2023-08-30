package SECCION_5;

public class Condicionales {

  public static void main(String[] args) {
    // if → si
    // else → sino
    // else if → sino si

    // String colorLuz = "Rojo";

    // if (colorLuz == "Verde") {
    // System.out.println("Puede continuar");
    // } else if (colorLuz == "Amarillo") {
    // System.out.println("Precaución");
    // } else if (colorLuz == "Rojo") {
    // System.out.println("Alto total");
    // } else {
    // System.out.println("No se reconoce el color");
    // }

    // Condiciones anidadas
    int promedio = 10;

    if (promedio >= 7) {
      if (promedio == 10) {
        System.out.println("Felicidades, excelente promedio");
      } else {
        System.out.println("Aprobado");
      }

    } else {
      System.out.println("Reprobado");
    }

  }
}
