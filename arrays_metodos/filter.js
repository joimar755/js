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

  /* for (let i = 0; i < producto.length; i++) {
    if (producto[i].title === "Agua") {
      console.log(producto[i]);
    }
  } */

const filter = producto.filter(item => {
    if (item.title === "Agua") {
        return true;
    }
})

console.log(filter); 