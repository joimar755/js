const producto = [
  {
    precio: 500,
    id: 1,
    title: "Café",
    thumbnailUrl: "https://picsum.photos/id/0/600",
  },
  {
    precio: 300,
    id: 2,
    title: "Pizza",
    thumbnailUrl: "https://picsum.photos/id/10/600",
  },
  {
    precio: 100,
    id: 3,
    title: "Agua",
    thumbnailUrl: "https://picsum.photos/id/20/600",
  },
  {
    precio: 50,
    id: 4,
    title: "Sandía",
    thumbnailUrl: "https://picsum.photos/id/30/600",
  },
  {
    precio: 10,
    id: 5,
    title: "Mango",
    thumbnailUrl: "https://picsum.photos/id/40/600",
  },
  {
    precio: 150,
    id: 6,
    title: "Chela",
    thumbnailUrl: "https://picsum.photos/id/50/600",
  },
];

const tabla = document.getElementById("tabla");
tabla.innerHTML = "";
producto.forEach((element) => {
  tabla.innerHTML += `
       <div class="col-2">
      <div class="p-3 card">
        <img src="${element.thumbnailUrl}" class="card-img-top  d-block mx-auto" alt="${element.title}">
        <h5 class="card-title">${element.title}</h5>
        <p class="card-text">Precio: ${element.precio}</p>
        <button type="button" class="btn btn-primary">añadir</button>
      </div>
    </div>
    `;
});
