//Dado un array de productos con su precio, incrementa el precio de cada producto en un 10%.
const productos = [
    { nombre: "Manzanas", precio: 2.0 },
    { nombre: "Peras", precio: 3.0 },
    { nombre: "Bananas", precio: 1.5 }
  ];

 const precio = productos.map(item => {
    return{
        nombre: item.nombre,
        precio: Math.round(item.precio * 0.1 * 100) / 100
    }

  }); 
console.log(precio);
