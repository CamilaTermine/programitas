palabra = input("ingrese una palabra: ");
invertida = "";

for i in range (0, len(palabra)):
    invertida = palabra[i] + invertida;

print(f"la palabra es {invertida}");


