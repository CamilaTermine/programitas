palabra = input("ingrese una palabra: ");
letra1 = "";
letra2 = "";
repetido = False;

for i in range(0, len(palabra)):
    letra1 = palabra[i];
    for i2 in range (i+1, len(palabra)):
        letra2 = palabra[i2];
        if letra1 == letra2: 
            repetido = True;

if repetido == False:
    print(f"la palabra {palabra} no tiene letras repetidas");
else:
    print(f"la palabra {palabra} tiene letras repetidas");
