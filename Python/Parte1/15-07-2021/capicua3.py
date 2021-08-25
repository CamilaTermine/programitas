palabra = input("ingrese una palabra: ");
palabra2 = len(palabra)-1;
capicua = True;

for i in range (0, int(len(palabra)/2)):
    if palabra[i] != palabra[palabra2]:
        capicua = False;
    palabra2 = palabra2-1;

if capicua == True:
    print(f"la palabra {palabra} es capicua");
else:
    print(f"la palabra {palabra} no es capicua");


