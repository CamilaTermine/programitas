let numeros = parseInt(prompt("cuantos numeros desea ingresar"));
let numeromayor = 0;


for (let contador = 0; contador < numeros; contador++) {
    let numero = parseInt(prompt("ingrese un numero"));
    if (contador != 0) {
        if (numero > numeromayor) {
            numeromayor = numero;
        }
    } else {
        numeromayor = numero;
    } 
}
if (numeros == 0) {
    document.write("no hay numeros")
} else {
    document.write (numeromayor);
}
