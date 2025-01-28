//Dado un array de nombres, convierte cada nombre a mayúsculas.
const nombres = ["juan", "maría", "carlos", "ana"];
const mayúsculas = nombres.map((item) => {
    return item.toUpperCase();
})

console.log(mayúsculas);

//Dado un array con palabras repetidas, devuelve un objeto que cuente cuántas veces aparece cada palabra.
const palabras = ["rojo", "azul", "rojo", "verde", "azul", "rojo"];
const count = palabras.reduce((acc, item) => {
    if (acc[item]) {
        acc[item] ++;
    } else {
        acc[item] = 1;
    }
    return acc;
    
}, {})

console.log(count);