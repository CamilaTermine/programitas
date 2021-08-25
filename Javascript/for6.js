let numero = parseInt(prompt("ingrese un numero"));
let n0 = 0;
let n1 = 1;


for (let contador = 0; contador <= numero; contador++) {
    if (contador == 0) {
        n0 = 0;
    } 
    if (contador == 1) {
        n0 = 1;
    } else if (contador > 1){
        let n0v = n0
        n0 = n1
        n1 = n0v + n1
    }
       
}   
document.write (n0);




