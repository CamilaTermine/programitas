#2) Calcular e imprimir la suma de los números enteros comprendidos entre dos números enteros A y B ingresados por teclado (A y B también se incluyen en la suma). 
# Tener en cuenta que A puede ser mayor, menor o igual que B. Por ejemplo A=2 y B=5. La suma es de 2+3+4+5=14


#a = int(input("ingrese el numero A:"));
#b = int(input("ingrese el numero B:"));
#suma = 0;
#num1 = a;
#num2 = b;


#if a > b:
    #num1 = b
    #num2 = a
#or i in range (num1, num2+1):
#        suma = suma + i
#print(f" la suma es: {suma}");


a = int(input("ingrese el numero A:"));
b = int(input("ingrese el numero B:"));
suma = 0;
num1 = a;
num2 = b;

if a > b:
    num1 = b;
    num2 = a;
while num1 <= num2:
    suma = suma + num1;
    num1 = num1+1;
print(f" la suma es: {suma}");