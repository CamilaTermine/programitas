palabra = input("ingrese una palabra: ");
mitadPalabra = "";
mitadPalabra2 = "";
contador2 = 0;
par = False;

if len(palabra) % 2 == 0:
    par = True;
    for i in range (0, int((len(palabra)/2))):
        mitadPalabra = mitadPalabra + palabra[i];
        contador2 = i;
    for i2 in range(len(palabra)-1, contador2, -1):
        mitadPalabra2 = mitadPalabra2 + palabra[i2];
else:
    for i in range (0, int((len(palabra)/2)+1)):
        mitadPalabra = mitadPalabra + palabra[i];
        contador2 = i;
    for i2 in range(len(palabra)-1, contador2-1, -1):
        mitadPalabra2 = mitadPalabra2 + palabra[i2];


if mitadPalabra == mitadPalabra2:
    print(f"la palabra {palabra} es capicua")
else:
    print(f"la palabra {palabra} no es capicua")
    


