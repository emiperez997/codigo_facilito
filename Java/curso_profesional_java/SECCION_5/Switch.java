package SECCION_5;

public class Switch {

  public static void main(String[] args) {
    // switch → interruptor
    // case → caso
    // break → romper
    // default → por defecto

    String colorLuz = "Rosa";

    switch (colorLuz) {
      case "Verde":
        System.out.println("Puede continuar");
        break;

      case "Amarillo":
        System.out.println("Precaución");
        break;

      case "Rojo":
        System.out.println("Alto total");
        break;

      default:
        System.out.println("No se reconoce el color");
        break;
    }
  }
}
