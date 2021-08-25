num = int(input("ingrese un numero: "));
divisor = 0;

for i in range (1, num):
    if num % i == 0:
        divisor = divisor + i;

if divisor == num:
    print(f"el numero {num} es perfecto");
else:
    print(f"el numero {num} no es perfecto");