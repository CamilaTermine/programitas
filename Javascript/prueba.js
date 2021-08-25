let numero = parseInt(prompt("ingrese un numero"));

for (let contador = 1; contador <= numero; contador++) {

    for (let contador2 = 1; contador2 <= contador; contador2++) {

        document.write(contador2);

    }
    document.write("<br>");
}