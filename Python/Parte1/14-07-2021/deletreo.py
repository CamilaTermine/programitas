texto = input("ingrese una palabra: ");
largo = len(texto);
deletreo = ""


for i in range (0,largo):
    deletreo = deletreo + texto[i] + " ";

print(f"la palabra {texto} deletreada es: {deletreo}");