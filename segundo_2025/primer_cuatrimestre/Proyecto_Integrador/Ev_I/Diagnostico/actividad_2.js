const persona = { nombre: "Lucía", edad: 28, profesión: "Diseñadora" };

// 1. Mostrar mensaje usando desestructuración
const { nombre, edad, profesión } = persona;
console.log(`${nombre} tiene ${edad} años y trabaja como ${profesión}.`);

// 2. Agregar una nueva propiedad al objeto
persona.ciudad = "Rosario";

// Opcional: Mostrar el objeto actualizado para verificar
console.log(persona);