let anioActual = parseInt(prompt("ingrese el anio actual"));
let edad = parseInt(prompt("ingrese su edad"));
let sexo = prompt("ingrese su sexo");


if (edad < 18) {
    document.write("sos menor de edad<br>");
    document.write("no podes votar");

} else {
    document.write("sos mayor de edad<br>");
    if (anioActual > 1952) {
        document.write("podes votar");
    } else {
        if (sexo != "masculino") {
            document.write("no podes votar");

        } else {
            document.write("podes votar");
        }
    } 

}
