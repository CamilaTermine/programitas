let numero = parseInt(prompt("ingrese un numero"));
let n0 = 0;
let n1 = 1;


for (let contador = 0; contador <= numero; contador++) {
    if (contador == 0) {
        n1 = 0;
    } 
    if (contador == 1) {
        n1 = 1;
    } else {
        let n0v = n0
        n0 = n1
        n1 = n0v + n0
    }
       
}   
document.write (n1);




