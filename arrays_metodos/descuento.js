//Dado un array de productos, filtra aquellos cuyo precio sea mayor a $10, aplícales un descuento del 20%, y devuelve el array resultante con los precios actualizados.
const productos = [
    { nombre: "Manzana", precio: 5 },
    { nombre: "Televisor", precio: 300 },
    { nombre: "Camiseta", precio: 20 },
    { nombre: "Lapicero", precio: 2 }
  ];
  const filter_Productos = productos
.filter(item => item.precio > 10)
.map(item => (item.precio = Math.round(item.precio - item.precio * 0.2), item))
console.log('Productos con precio mayor a $10 y con descuento del 20%: ');
console.log(filter_Productos); 

//Dado un array de productos con sus categorías, crea un objeto que cuente cuántos productos hay por categoría.
const productos1 = [
    { nombre: "Pelota", categoria: "deporte" },
    { nombre: "Mochila", categoria: "escolar" },
    { nombre: "Cuerda", categoria: "deporte" },
    { nombre: "Cuaderno", categoria: "escolar" },
    { nombre: "Silla", categoria: "hogar" }
  ]; 
  const categorias = productos1.map(item => item.categoria);
  const count = categorias.reduce((acc, item) => {
    if (acc[item]) {
        acc[item] ++;
    } else {
        acc[item] = 1;
    }
    return acc;
    
}, {})
console.log('Productos por categoría: ');
console.log(count); 
//Dado un array de productos, ordénalos de mayor a menor precio. Usa map después de ordenarlos para devolver solo los nombres de los productos.
const productos2 = [
    { nombre: "Manzana", precio: 5 },
    { nombre: "Televisor", precio: 300 },
    { nombre: "Camiseta", precio: 20 },
    { nombre: "Lapicero", precio: 2 }
  ];
 const array = productos2
 .sort((a, b) => a.precio - b.precio)
 .map(item => item.nombre)
console.log('Productos ordenados de mayor a menor precio: ');
 console.log(array)