//Dado un array de objetos que representan productos en un carrito de compras, calcula el total a pagar.
const carrito = [
    { producto: "Faja lumbar", precio: 50, cantidad: 2 },
    { producto: "Banda elástica", precio: 30, cantidad: 1 },
    { producto: "Rodillera", precio: 40, cantidad: 3 }
  ];

  const suma = carrito.reduce((total, item) => total + item.precio * item.cantidad  , 0)
console.log(`El total a pagar es: ${suma}`);


const productos = [
    { nombre: "Pelota", precio: 20, categoria: "deporte" },
    { nombre: "Mochila", precio: 50, categoria: "escolar" },
    { nombre: "Cuerda", precio: 15, categoria: "deporte" },
    { nombre: "Cuaderno", precio: 5, categoria: "escolar" }
  ]; 
const filter = productos.filter(item => {
    if (item.categoria === "deporte") {
        return true;
    }
})


const suma_cat = filter.reduce((total, item) => total + item.precio, 0)

//console.log(filter);
console.log(`El total de la categoria deporte es: ${suma_cat}`); 


const pacientes = [
    { nombre: "Juan", citaActiva: true },
    { nombre: "María", citaActiva: false },
    { nombre: "Carlos", citaActiva: true },
    { nombre: "Ana", citaActiva: false }
  ];
const filter_citas = pacientes
.filter(item => item.citaActiva === true)
.map(item => (item.nombre.toUpperCase()))
console.log('Pacientes con cita activa:');
console.log(filter_citas);
