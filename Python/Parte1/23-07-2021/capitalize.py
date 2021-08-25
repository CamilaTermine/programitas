palabra = input("ingrese un texto: ");
subPalabra = ""
caps = ""

for i in range (0, len(palabra)):
    if palabra[i] !=" ":
        subPalabra = subPalabra + palabra[i]
    else:
        caps = caps + subPalabra.capitalize() + " ";
        subPalabra = "";
caps = caps + subPalabra.capitalize()

print(caps)