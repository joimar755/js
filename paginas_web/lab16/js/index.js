function mostrarimagen(event) {
    let imagen = document.getElementById('ver-img')
    imagen.src = URL.createObjectURL(event.target.files[0])
}


document.getElementById('formulario-registro').addEventListener('submit', function(event){
  event.preventDefault()
  const inf ={
     nombre : document.getElementById('nombre').value,
     correo : document.getElementById('email').value,
     password: document.getElementById('password').value,
     imagen : document.getElementById('file-img').files[0]
  }
  
  if (inf.nombre === '' || inf.correo === '' || inf.password === '') {
    alert('Todos los campos son obligatorios')
    return
  }
  const formatosValidos = ["image/jpeg", "image/png"];

   if (!formatosValidos.includes(inf.imagen.type)) {
    alert('Solo se permiten imágenes en formato JPEG o PNG')
    return
  }
  console.log(inf)

})
