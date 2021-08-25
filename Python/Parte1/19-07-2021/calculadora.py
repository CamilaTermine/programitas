#1-usuario pide un numero
#2-el programa muestra el resultado parcial
#3-el programa muestra un menu con 5 opciones
#   opcion 0: la opcion 0 va a ser terminar el programa
#   opcion 1: sumar
#   opcion 2: restar
#   opcion 3: multiplicar
#   opcion 4: dividir
#4-repetir el ciclo

num1 = int(input("ingrese un numero: "));
print(f"el resultado parcial del numero es {num1}");
iniciador = True;
resultado = num1


while iniciador == True:
    opcion = int(input("ingrese la accion que desea realizar:\n 0- terminar el programa \n 1- sumar \n 2- restar \n 3- multiplicar \n 4- dividir\n "))
    if opcion == 0:
        iniciador = False;
    else:
        num2 = int(input("ingrese otro numero: "));
        if opcion == 1:
            resultado = resultado+num2;
        if opcion == 2:
            resultado = resultado-num2;
        if opcion == 3:
            resultado = resultado*num2;
        if opcion == 4:
            while num2 == 0:
                num2 = int(input("no se puede dividir por 0, ingrese otro numero: "))
            resultado = resultado/num2;
    print(f"el resultado es: {resultado}");