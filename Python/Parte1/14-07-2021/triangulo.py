mensaje = "*"
altura = int(input("ingrese la altura deseada: "));

for i in range (0, altura):
    for i2 in range (0,i):
        mensaje = mensaje + "*"
    mensaje = mensaje + '\n'

for i in range (0, altura):
    for i2 in range (altura - i):
        mensaje = mensaje + "*"
    mensaje = mensaje + '\n'

print(f"{mensaje}")
