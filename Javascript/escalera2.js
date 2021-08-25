let numero = parseInt(prompt("ingrese un numero"));
let n1 = numero;

for (let contador = 0; contador < numero; contador++) {
    for (let c2 = n1; c2 >=1; c2--) {
        document.write(c2);
    }
    n1 = n1-1;
    document.write("<br>");
}