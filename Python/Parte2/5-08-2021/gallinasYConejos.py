#proverbio chino: 
conejos = 0;
gallina = 0;
cantCabezas = int(input("ingrese cantidad de cabezas: "));
cantPatas = int(input("ingrese cantidad de patas: "))

for i in range(0, cantPatas):
    conejo = i;
    for i2 in range (0, cantPatas):
        gallina = i2;
        if (conejo * 4) + (gallina * 2) == cantPatas and conejo + gallina == cantCabezas:
            print(f"la cantidad de conejos es {conejo} y la cantidad de gallinas es {gallina}")
