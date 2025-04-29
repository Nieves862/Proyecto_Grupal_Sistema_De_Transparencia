const numeros = [3, 7, 12, 5, 2];

// Usando map para obtener los números al cuadrado
const numerosAlCuadrado = numeros.map(numero => numero * numero);
console.log("Números al cuadrado:", numerosAlCuadrado);

// Usando filter para obtener los números mayores a 5
const numerosMayoresQueCinco = numeros.filter(numero => numero > 5);
console.log("Números mayores que 5:", numerosMayoresQueCinco);

// Función flecha para determinar si un número es par o impar
const esParOImpar = numero => (numero % 2 === 0 ? "par" : "impar");

// Ejemplo de uso de la función flecha
console.log("El número 10 es:", esParOImpar(10));
console.log("El número 1 es:", esParOImpar(1));