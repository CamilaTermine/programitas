palabra = input("ingrese un texto: ");
subPalabra = ""
caps = ""

for i in range (0, len(palabra)):
    if palabra[i] !=" ":
        subPalabra = subPalabra + palabra[i]
    if palabra[i] == " " or i == (len(palabra)-1):
        caps = caps + subPalabra.capitalize() + " ";
        subPalabra = "";
print(caps)


