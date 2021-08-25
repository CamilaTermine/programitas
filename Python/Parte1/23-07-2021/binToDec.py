bin = input("ingrese un numero binario: ");
numP = 0;

for i in range (len(bin)-1, -1, -1):
        numP = numP + int(bin[i])*(2**i);
print(numP);