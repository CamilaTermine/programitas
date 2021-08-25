listaPar = [1, 3, 4, 5, 9];
listaImpar = [2, 4, 6, 7, 10];
listaOrdenada = [];
indicePar = 0;
indiceImpar = 0;
numeroParcial = 0;
maschikito = 0;



while len(listaOrdenada) != len(listaPar + listaImpar):
    if indicePar == len(listaPar):
        listaOrdenada.append(listaImpar[indiceImpar]);
        indiceImpar = indiceImpar + 1;
    elif indiceImpar == len(listaImpar):
        listaOrdenada.append(listaPar[indicePar]);
        indicePar = indicePar + 1;
    else:
        if listaPar[indicePar] < listaImpar[indiceImpar]:
            listaOrdenada.append(listaPar[indicePar]);
            indicePar = indicePar + 1;
        else:
            listaOrdenada.append(listaImpar[indiceImpar]);
            indiceImpar = indiceImpar + 1;
print(listaOrdenada);