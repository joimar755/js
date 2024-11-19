function monto() {
  const monto = 100;

  if (monto >= 100) {
    let descuento = monto * 0.1;
    let monto_f = monto - descuento;

    console.log(descuento);
    console.log("monto final es ", monto_f);
  } else {
    console.log("no aplica descuento");
  }
}

monto();
