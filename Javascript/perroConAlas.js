let ciclar = true;
let numero = 0;

while (ciclar == true) {
    numero = parseInt(prompt("ingrese un numero"));
    if (numero % 2 !=0) {
        document.write(numero+"<br>");
    } else {
        ciclar = false;
    }
} 