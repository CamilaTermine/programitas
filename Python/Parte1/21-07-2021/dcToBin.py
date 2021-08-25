num1 = int(input("ingrese un numero: "));
resParcial = num1;
bin = "";

if num1 > 0:
    while resParcial > 1:
        if resParcial % 2 == 0:
            bin = "0" + bin;
        else:
            bin = "1" + bin;
        resParcial = int(resParcial / 2);
bin = str(resParcial) + bin;

print(bin);