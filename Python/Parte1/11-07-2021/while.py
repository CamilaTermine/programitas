contador = 3;
suma = 0;

while contador != 0:
    numero = int(input("ingrese un numero: "));
    suma = suma + numero;
    contador = contador -1;

print(f"el resultado es {suma}");