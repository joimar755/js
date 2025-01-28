//Dado un array de estudiantes con sus notas, filtra solo los estudiantes que hayan aprobado (nota >= 3.0).
const estudiantes = [
    { nombre: "Juan", nota: 4.5 },
    { nombre: "María", nota: 2.8 },
    { nombre: "Carlos", nota: 3.2 },
    { nombre: "Ana", nota: 1.9 }
  ];

const filter = estudiantes.filter(item => {
    if (item.nota >= 3.0) {
        return true;
    } 
}).map(item => ({
    ...item,
    aprobado: true
  }))

console.log(filter); 