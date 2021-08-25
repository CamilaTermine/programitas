let numero = parseInt(prompt("ingrese un numero"));
let contador = 0;
let par = false;

if (numero%2==0) {
    par = true;
} 

while (contador <= numero) {
    if (contador%2==0 && par == true) {
        document.write(contador + "<br>");
    } else {
        if (contador%2!=0 && par == false)
        document.write(contador + "<br>");
    }
    contador = contador+1;
}
