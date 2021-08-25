palabraSecreta = "uwu";
palabraEncriptada = "";
vidas = 7;
acertar = False;
auxiliar = "";

for i in range (0, len(palabraSecreta)):
    palabraEncriptada = palabraEncriptada + "*";
print(palabraEncriptada);

while vidas > 0 and palabraEncriptada != palabraSecreta:
    acertar = False;
    letraRandom = input("ingrese una letra: ");
    auxiliar = "";
    for i in range (0, len(palabraSecreta)):
        if palabraSecreta[i] == letraRandom:
            auxiliar = auxiliar + letraRandom;
            acertar = True;
        else:
            auxiliar = auxiliar + palabraEncriptada[i];
    if acertar == False:
        vidas = vidas -1;

    palabraEncriptada = auxiliar;
    print(f"{palabraEncriptada} / te quedan {vidas} vidas");
if palabraEncriptada == palabraSecreta:
    print(f"ganaste, la palabra era {palabraSecreta}");
else:
    print(f"perdiste, la palabra era {palabraSecreta}");



