#guardar en una lista n numeros randoms
#mostrar la lista y el promedio
import random
arreglo = [];
cantNum = int(input("indique la cantidad de numeros que quiere en su arreglo: "));
suma = 0;
promedio = 0;

for i in range (0, cantNum):
    numero = random.randint(0, 10);
    arreglo.append(numero);
    suma = suma + numero;
promedio = suma / cantNum

print(f"la lista de numeros es: {arreglo} \n y el promedio es {promedio}")
