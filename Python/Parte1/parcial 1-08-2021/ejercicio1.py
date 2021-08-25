#1) Escribir un programa en formato .py para ingresar los años de antigüedad de los empleados de una empresa. 
#El fin de los datos se indica ingresando -1. Se solicita imprimir un informe que contenga:
#- Cantidad total de empleados de la empresa.
#- Cantidad de empleados de cada grupo: Nivel 1  (1 a 10 años de antigüedad), Nivel 2 (11 a 20 años de antigüedad), Nivel 3  (a partir de los 21 años).
#- Porcentaje de personas que ya  tienen los 30 años de antigüedad en el establecimiento.
#El valor de antigüedad más pequeño y el más grande.

cantEmpleados = 0;
antiguedad = 0;
nivel1 = 0;
nivel2 = 0;
nivel3 = 0;
maxAntiguedad = 0;
porcentajeMaxAntiguedad = 0;
iniciador = True;
antiguedadMayor = 0;
antiguedadMenor = 0;


while iniciador == True:   
        antiguedad = int(input("ingrese la antiguedad del empleado. Si desea finalizar el programa ingrese -1: "));
        if antiguedad == -1:
            iniciador = False;
        else:
            if cantEmpleados == 0:
                antiguedadMenor = antiguedad;
                antiguedadMayor = antiguedad;
            cantEmpleados = cantEmpleados + 1;
            if antiguedad < antiguedadMenor:
                antiguedadMenor = antiguedad
            if antiguedad > antiguedadMayor:
                antiguedadMayor = antiguedad
            if antiguedad > 0 and antiguedad < 11:
                nivel1 = nivel1 + 1;
            if antiguedad > 10 and antiguedad < 21:
                nivel2 = nivel2 +1; 
            if antiguedad > 20:
                nivel3 = nivel3 +1;
                if antiguedad >= 30:
                    maxAntiguedad = maxAntiguedad +1;
if cantEmpleados >= 1:
    porcentajeMaxAntiguedad = int((maxAntiguedad*100)/cantEmpleados);           
    print(f"la cantidad de empleados es de {cantEmpleados} de los cuales {nivel1} pertenecen al Nivel 1, {nivel2} pertenecen al Nivel 2 y {nivel3} pertenecen al Nivel 3 de antiguedad. \n el porcentaje de personas que ya tienen 30 años de antiguedad es de : {porcentajeMaxAntiguedad}%. \n La antiguedad menor en la empresa es de {antiguedadMenor} años y la antiguedad mayor en la empresa es de {antiguedadMayor} años.")
else:
    print ("usted no tiene empleados")
