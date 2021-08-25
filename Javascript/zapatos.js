// para una tienda de zapatos que tiene una promoción de descuento 
// para vender al mayor, esta dependerá del número de zapatos que se compren. 
// Si son más de diez, se les dará un 10% de descuento sobre el total de la compra; 
// si el número de zapatos es mayor de veinte pero menor de treinta, 
// se le otorga un 20% de descuento; y si son más treinta zapatos se otorgará un 40% de 
// descuento. El precio de cada zapato es de $80.

let cantidad = parseInt(prompt("ingrese cantidad de zapatos a comprar"));
let precioUnidad = 80;
let precioTotal = cantidad * precioUnidad;
let precioFinal = 0;

if (cantidad > 10) { 
    if (cantidad > 20) {
        if (cantidad > 30) {
            precioFinal = precioTotal - (precioTotal * 0.4);
        } else {
            precioFinal = precioTotal - (precioTotal *0.2);
        }
    } else {
        precioFinal = precioTotal - (precioTotal*0.1);
    }
    // if (cantidad <= 20) {
    //     precioFinal = precioTotal - (precioTotal * 0.1); 
    // } else {
    //     if (cantidad > 20 && cantidad < 30) {
    //         precioFinal = precioTotal - (precioTotal * 0.2);
    //     } else {
    //         precioFinal = precioTotal - (precioTotal * 0.4);
    //     }
    // }
} else {
    precioFinal = precioTotal;
}
             
document.write(precioFinal);


