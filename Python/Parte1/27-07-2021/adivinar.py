numSecreto = "1892";
numRandom = "";
vidas = 10;
signo = "";


while vidas > 0 and numRandom != numSecreto:
    numRandom = input("ingrese un numero: ");
    signo = "";
    for i in range (0, 4):
        if numSecreto[i] == numRandom[i]:
            signo = signo + "+";
        elif numRandom[i] in (numSecreto[0], numSecreto[1], numSecreto[2], numSecreto[3]):
            signo = signo + "-";
    vidas = vidas -1;
    print(f"{numRandom} || {signo} \n");

if numRandom != numSecreto:
    print(f"usted ha perdido, el numero era {numSecreto}");
else :
    print(f"usted ha ganado, el numero es {numSecreto}");


