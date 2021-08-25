let numero = parseInt(prompt("ingrese un numero del 1 al 10"))
let producto = 1;
let resultado = 0;

while (producto < 11) {
    resultado = numero*producto;
    let tabla = numero + "x" + producto + "=";
    document.write(tabla + resultado + "<br>");
    producto = producto + 1;
}


