numero = int(input("ingrese un numero: "));
mensaje = "";

for i in range(numero, 0, -1):
    for i2 in range(i, 0, -1):
        mensaje = mensaje + str(i2);
    mensaje = mensaje + "\n";
    
print(mensaje);