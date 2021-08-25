def menu():
    print("elija la accion que desea realizar:")
    print("1.suma")
    print("2.resta")
    print("3.multiplicacion")
    print("4.division")
    print("0.salir del programa")

def suma(a, b):
    resultado = a + b;
    return resultado;

def resta(a, b):
    resultado = a - b;
    return resultado;

def multiplicacion(a, b):
    resultado = a * b;
    return resultado;

def division(a, b):
    while b == 0:
        b = int(input("No se puede realizar la operacion. Ingrese otro numero: ")) 
    resultado = a/b;
    return resultado;


num1 = int(input("ingrese el primer numero: "));
iniciador = True;
resultado = num1;


while iniciador == True:
    menu()
    opcion = int(input())
    if opcion == 0:
        iniciador = False;
        print(f"el resultado final es {resultado}");
    else:
        num2 = int(input("ingrese el segundo numero: "));
        if opcion == 1:
            resultado = suma(resultado,num2);
        if opcion == 2:
            resultado = resta(resultado,num2);
        if opcion == 3:
            resultado = multiplicacion(resultado,num2);
        if opcion == 4:
            resultado = division(resultado,num2);
        print(f"el resultado parcial es {resultado}");

        



