ciclar = True;
suma = 0;

while ciclar == True:
    numero = int(input("ingrese un numero: "));
    if numero != 0:
        suma = suma + numero;
    else: 
        ciclar = False
print(f"el resultado es: {suma}");
