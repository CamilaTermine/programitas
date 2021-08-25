let numero = parseInt(prompt("ingrese un numero natural"));
let contador = 2;
let primo = true;

while (contador< numero && primo == true) {
    if (numero%contador == 0) {
        primo = false;
    } 
    contador = contador+1;
}

if (primo == false  || numero == 1) {
    document.write("no es primo");
} else {
    document.write("es primo");
}
