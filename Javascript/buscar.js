let numeros = parseInt(prompt("cuantos numeros desea ingresar"));
let numeromayor = 0;
let numeromenor = 0;
let promedio = 0;

for (let contador = 0; contador < numeros; contador++) {
    let numero = parseInt(prompt("ingrese un numero"));
    if (contador == 0) {
        numeromayor = numero;
        numeromenor = numero;
    } else {
        if (numero > numeromayor) {
            numeromayor = numero;
        }
        if (numero < numeromenor) {
            numeromenor = numero;
        }
    }
    promedio = promedio+numero
}
if (numeros == 0) {
    document.write("no hay numeros");
} else {
    document.write ("el numero mayor es " + numeromayor + "<br>" + "el numero menor es " + numeromenor + "<br>" + "el promedio es " + (promedio/numeros));
}
