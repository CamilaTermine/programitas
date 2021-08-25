fecha = input("ingrese una fecha en formato dd/mm/aaaa: ");
dia = fecha[0] + fecha[1];
diaInt = int(dia);
mes = fecha[3] + fecha[4];
mesInt = int(mes);
año = fecha[6] + fecha[7] + fecha[8] + fecha[9];
añoInt = int(año);
fechaSig = "";

if mesInt in (1, 3, 5, 7, 8, 10, 12):
    if diaInt < 31:
        dia = str(diaInt + 1);
    elif mesInt != 12:
        dia = "01";
        mes = str(mesInt + 1);
    else:
        dia = "01";
        mes = "01";
        año = str(añoInt + 1);
elif mesInt in (4, 6, 9, 11):
    if diaInt < 30:
        dia = str(diaInt + 1);
    else:
        dia = "01";
        mes = str(mesInt + 1);
elif diaInt < 27:
    dia = str(diaInt + 1);
else:
    dia = "01";
    mes = str(mesInt + 1);
fechaSig = dia + "/" + mes + "/" + año;
print(f"la fecha siguiente es {fechaSig}");

        


