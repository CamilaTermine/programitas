palabra = input("ingrese una palabra: ");
largo = len(palabra);
cantConsonantes = 0;


for i in range(0, largo):
    if palabra[i] != "a" and palabra[i] != "e" and palabra[i] != "i" and palabra[i] != "o" and palabra[i] != "u":
        cantConsonantes = cantConsonantes + 1;


print(f"la palabra {palabra} tiene {cantConsonantes} consonantes")