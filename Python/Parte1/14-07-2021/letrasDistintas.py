palabra = input("ingrese una palabra: ");
largo = len(palabra);
cantA = 0;
cantE = 0;
cantI = 0;
cantO = 0;
cantU = 0;


for i in range(0, largo):
    if palabra[i] == "a":
        cantA = cantA+1
    if palabra[i] == "e":
        cantE = cantE+1
    if palabra[i] == "i":
        cantI = cantI+1
    if palabra[i] == "o":
        cantO = cantO+1
    if palabra[i] == "u":
        cantU = cantU+1

if cantA >1 or cantE >1 or cantI >1 or cantO >1 or cantU >1:
    print("tiene vocales repetidas");
else:
    print("no tiene vocales repetidas");
    

