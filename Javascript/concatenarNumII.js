let nota1 = parseInt(prompt("ingrese la primer nota"));
let nota2 = parseInt(prompt("ingrese la segunda nota"));
let nota3 = parseInt(prompt("ingrese la tercer nota"));

if (nota1 > nota2) {
    if (nota1 > nota3) {
        document.write(nota1);
    } else {
        document.write(nota3);
    }
} else {
    if (nota2 > nota3) {
        document.write(nota2);
    } else {
        document.write(nota3);
    }
} 
