let numero = parseInt(prompt("ingrese un numero"));
let numeroInicial = numero;

for (let contador = 0; contador < numero; contador++) {
    for (let contador2 = numeroInicial; contador2 >= 1; contador2--) {
        document.write (contador2);

    } 
    numeroInicial = numeroInicial-1;
    document.write("<br>");
}