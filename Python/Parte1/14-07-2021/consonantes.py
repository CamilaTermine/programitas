palabra = input("ingrese una palabra: ");
largo = len(palabra);
cantConsonantes = 0;


for i in range(0, largo):
    if not(palabra[i] == "a" or palabra[i] == "e" or palabra[i] == "i" or palabra[i] == "o" or palabra[i] == "u"):
        cantConsonantes = cantConsonantes + 1;


print(f"la palabra {palabra} tiene {cantConsonantes} consonantes")
    
    
