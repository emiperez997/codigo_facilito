package SECCION_3;

class Operadores {

  public static void main(String[] args) {
    // Operadores aritméticos
    int variableX = 50, variableY = 10;
    int resultado;

    resultado = variableX + variableY;
    System.out.println("Suma: " + resultado);

    resultado = variableX - variableY;
    System.out.println("Resta: " + resultado);

    resultado = variableX * variableY;
    System.out.println("Multiplicación: " + resultado);

    resultado = variableX / variableY;
    System.out.println("División: " + resultado);

    // ++ → Incrementa en uno
    // -- → Decrementa en uno
    variableX++; // → variableX = variableX + 1;
    System.out.println("Incremento: " + variableX);
    variableX--; // → variableX = variableX - 1;
    System.out.println("Decremento: " + variableX);

    variableX += 100; // → variableX = variableX + 100;
    System.out.println("Suma: " + variableX);

    variableX -= 100; // → variableX = variableX - 100;
    System.out.println("Resta: " + variableX);

    variableX *= 100; // → variableX = variableX * 100;
    variableX /= 100; // → variableX = variableX / 100;

  }
}