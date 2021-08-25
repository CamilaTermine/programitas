let numero = parseInt(prompt("Ingrese un numero"));

if (numero < 0) {
    numero = Math.sqrt(numero**2);
    document.write(numero);
} else {
    document.write(numero);
}
