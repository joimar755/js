function Calculadora(n1, n2, operacion) {
  if (operacion === "suma") {
    console.log(n1 + n2);
  } else if (operacion === "resta") {
    console.log(n1 - n2);
  } else if (operacion === "multi") {
    console.log(n1 * n2);
  } else if (operacion === "div") {
    if (n2 != 0) {
      console.log(n1 / n2);
    } else {
      console.log("Error: División por cero");
    }
  } else {
    console.log("Error: Operación no válida");
  }
}

let next = true;

while (next) {
  const operacion = "multi";
  if (operacion.toLowerCase() === "fin") {
    next = false;
    console.log("fin del programa");
    break;
  }

  const n1 = 5;
  const n2 = 10;

  /* 
    Calculadora(5, 2, "suma");
    Calculadora(5, 2, "multi");
    Calculadora(5, 2, "resta");
    Calculadora(5, 0, "div");
    */
  Calculadora(n1, n2, operacion.toLowerCase());
  break;
}
