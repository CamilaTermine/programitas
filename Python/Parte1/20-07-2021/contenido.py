palabra1 = input("ingrese una palabra: ");
palabra2 = input("ingrese otra palabra: ");
palabrita = "";
contenido = False;

for i in range (0, len(palabra2)):
    for i2 in range (0, len(palabra1)- len(palabra2)):
        palabrita = "";
        if palabra1[i2] == palabra2[i]:
            for i3 in range (0, len(palabra2)):
                palabrita = palabrita + palabra1[i2+i3]
            if palabra2 == palabrita:
                contenido = True;
if contenido == True:
    print(f"la palabra {palabra2} esta contenida en {palabra1}");
else:
    print(f"la palabra {palabra2} no esta contenida en {palabra1}");
