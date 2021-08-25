palabra = input("ingrese una palabra: ");
mitadPalabra = "";
mitadPalabra2 = "";
contador2 = 0;

for i in range (0, (len(palabra))):
    mitadPalabra = mitadPalabra + palabra[i];

for i2 in range(len(palabra)-1, -1, -1):
    mitadPalabra2 = mitadPalabra2 + palabra[i2];

if mitadPalabra == mitadPalabra2:
    print(f"la palabra {palabra} es capicua")
else:
    print(f"la palabra {palabra} no es capicua")
    


