let anio = parseInt(prompt("ingrese un anio"))

if (anio % 4 == 0) {
    if (anio % 100 == 0) {
        if (anio % 400 == 0) {
            document.write("es biciesto");
        } else {
            document.write("no es biciesto");
        } 

    } else {
        document.write("es biciesto");
    }
} else {
    document.write("no es biciesto");
}




// if (anio % 4 == 0 && anio % 100 != 0) {
//     document.write("es biciesto");
// } else {
//     if (anio % 400 == 0) {
//         document.write("es biciesto");
//     } else {
//         document.write("no es biciesto");
//     }
// }