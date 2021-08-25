import random
arreglo = [];
cantNum = int(input("indique la cantidad de numeros que quiere en su arreglo: "));
suma = 0;
promedio = 0;
numPos = 0;

for i in range (0, cantNum):
    numero = random.randint(-10, 10);
    arreglo.append(numero);
    if numero >= 0:
        suma = suma + numero;
        numPos = numPos + 1;
promedio = suma / numPos;

print(f"la lista de numeros es: {arreglo} \n y el promedio es {promedio}")
