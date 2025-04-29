const productos = [
    { nombre: "Notebook", precio: 1200 },
    { nombre: "Mouse", precio: 20 },
    { nombre: "Teclado", precio: 50 },
    { nombre: "Monitor", precio: 300 },
    { nombre: "Auriculares", precio: 80 },
  ];
  
  // 1. Usar filter para obtener solo los productos cuyo precio sea mayor a 100.
  const productosMayorA100 = productos.filter(producto => producto.precio > 100);
  console.log("Productos con precio mayor a $100:", productosMayorA100);
  
  // 2. Usar map para obtener un nuevo array de strings con el siguiente formato: "Notebook: $1200"
  const productosConFormato = productos.map(producto => `${producto.nombre}: $${producto.precio}`);
  console.log("Productos con formato:", productosConFormato);
  
  // 3. Usar reduce para calcular el precio total de todos los productos.
  const precioTotal = productos.reduce((acumulador, producto) => acumulador + producto.precio, 0);
  console.log("Precio total de todos los productos:", precioTotal);
  
  // 4. Combinar filter y map para obtener los nombres de los productos que cuesten menos de 100, todo en minúsculas.
  const nombresProductosMenorA100 = productos
    .filter(producto => producto.precio < 100)
    .map(producto => producto.nombre.toLowerCase());
  console.log("Nombres de productos con precio menor a $100 (en minúsculas):", nombresProductosMenorA100);