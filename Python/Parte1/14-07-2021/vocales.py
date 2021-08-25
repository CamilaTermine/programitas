palabra = input("ingrese una palabra: ");
largo = len(palabra);
cantVocales = 0;


for i in range(0, largo):
    if palabra[i] == "a" or palabra[i] == "e" or palabra[i] == "i" or palabra[i] == "o" or palabra[i] == "u":
        cantVocales = cantVocales + 1;

print(f"la palabra {palabra} tiene {cantVocales} vocales")
    
    
