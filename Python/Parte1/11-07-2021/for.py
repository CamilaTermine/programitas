resultado = 0;
cantRep = int(input("ingrese la cantidad de numeros a sumar: "));

for i in range(0, cantRep):
    numero = int(input("ingrese un numero: "));
    resultado = resultado + numero;

print(f"el resultado es: {resultado}");1