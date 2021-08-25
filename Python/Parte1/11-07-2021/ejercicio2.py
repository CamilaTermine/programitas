numero = int(input("ingrese un numero: "));
mensaje = "";

for i in range(1, numero+1):
    for i2 in range(1, i+1):
        mensaje = mensaje + str(i2);
    mensaje = mensaje + "\n"
    
print(mensaje);