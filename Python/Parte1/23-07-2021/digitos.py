num = int(input("ingrese un numero: "));
digitos = 1
numParcial = num

if num >= 10:
    while numParcial / 10 >= 1:
        numParcial = int(numParcial / 10)
        digitos = digitos +1 
print(digitos);