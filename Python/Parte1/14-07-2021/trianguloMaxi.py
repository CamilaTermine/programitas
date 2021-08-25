altura = 5;
trianguloArriba = ""
trianguloMedio = "*"
trianguloAbajo = ""

for i in range (0, altura-1):
    for i2 in range (0,i):
        trianguloArriba = trianguloArriba + "*"
        trianguloAbajo = "*" + trianguloAbajo
    trianguloArriba = trianguloArriba + '\n'
    trianguloMedio = trianguloMedio + "*"
    trianguloAbajo = '\n'+ trianguloAbajo

print(f"{trianguloArriba}{trianguloMedio}{trianguloAbajo}")