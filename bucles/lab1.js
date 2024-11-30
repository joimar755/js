function calcular() {
 const numeros = [5,6,8,7];
 let suma = 0;
 let next = true;

 while (next) {
    const input = "FIN"
    if (input.toLowerCase() === "fin"){
        next = false
    }else{
        const numero = parseFloat(input)
        if (!isNaN(numero)){
            numeros.push(numero);
        } else {
            console.log("Debe ingresar un número válido");
            break;
        }
    }
 }
 if (numeros.length > 0 ) {
    for (let i = 0; i < numeros.length; i++) {
        suma += numeros[i];
    }
    //calcular promedio
    const promedio = suma / numeros.length;
    console.log("La suma de los números es: " + suma);
    console.log("El promedio de los números es: " + promedio);
 }else{
    console.log("No se ingresaron números");
 }

}
calcular()