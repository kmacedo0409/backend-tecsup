
// import isodd from "is-odd";
// esta es la forma de importar librerias de manera tradicional commons js
const isodd = require("is-odd");
const informacion = require("./info-adicional");
const esPar= isodd(15);

console.log("hola");
console.log(esPar);

// aqui utilizamos lo que hemos exportado desde el archivo info-adicionales

console.log(informacion.edad);
const saludo=informacion.saludar("Rigoberto");
console.log(saludo);

