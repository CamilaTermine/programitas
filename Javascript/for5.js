let cantidadASumar = parseInt(prompt("Ingrese cant de veces que quiere sumar un numero"));
let suma = 0;

for (let contador = 0; contador < cantidadASumar; contador++) {
    let numero = parseInt(prompt("ingrese un numero"));
    suma = suma + numero;
}

document.write(suma)

//primer iteracion, estado de las variables:
//numero = 2
//suma = 2

//segunda iteracion, estado de las variables:
//numero = 3
//suma = 5




//tercera iteracion, estado de las variables:
//numero = 8
//suma = 13
