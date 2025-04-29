function procesar(array, callback) {
    const nuevoArray = [];
    for (let i = 0; i < array.length; i++) {
      nuevoArray.push(callback(array[i]));
    }
    return nuevoArray;
  }
  
  // Ejemplo de uso:
  const numeros = [1, 2, 3];
  const duplicar = x => x * 2;
  const cuadrados = x => x * x;
  
  const numerosDuplicados = procesar(numeros, duplicar);
  console.log("Números duplicados:", numerosDuplicados); // Salida: Números duplicados: [ 2, 4, 6 ]
  
  const numerosAlCuadrado = procesar(numeros, cuadrados);
  console.log("Números al cuadrado:", numerosAlCuadrado); // Salida: Números al cuadrado: [ 1, 4, 9 ]
  
  const sumarUno = x => x + 1;
  const numerosMasUno = procesar(numeros, sumarUno);
  console.log("Números más uno:", numerosMasUno); // Salida: Números más uno: [ 2, 3, 4 ]