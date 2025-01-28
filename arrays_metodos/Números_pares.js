//Dado un array de números, filtra los números que son pares.
const numeros = [3, 7, 2, 8, 10, 45, 22, 13]; 

const filter = numeros.filter(item => {
    return item % 2 === 0 
})

console.log(filter); 