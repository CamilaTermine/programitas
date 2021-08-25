let numero = parseInt(prompt("ingrese un numero"));
let contador = 0;

while (contador <= numero) { 
    if (contador % 2 == 0) {
        document.write(contador + "<br>");
        
    } 
    contador = contador+1;
}