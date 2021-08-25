cantAlumnos = int(input("ingrese cantidad de alumnos: "));
mensaje = "";
notaMenor = 0;
notaMayor = 0;
nombreAlumnoNotaMenor = "";
nombreAlumnoNotaMayor = "";
sumaNotas = 0;


for i in range(0, cantAlumnos):
    nombreAlumno = input("ingrese el nombre del alumno: ");
    notaAlumno = int(input("ingrese la nota del alumno: "));
    sumaNotas = sumaNotas + notaAlumno

    if i == 0:
        notaMenor = notaAlumno;
        nombreAlumnoNotaMenor = nombreAlumno;
        notaMayor = notaAlumno;
        nombreAlumnoNotaMayor = nombreAlumno;
    else:
        if notaAlumno < notaMenor:
            notaMenor = notaAlumno;
            nombreAlumnoNotaMenor = nombreAlumno;
        if notaAlumno > notaMayor:
            notaMayor = notaAlumno;
            nombreAlumnoNotaMayor = nombreAlumno;

print(f"el alumno {nombreAlumnoNotaMenor} con la nota {notaMenor} fue la mas baja");
print(f"el alumno {nombreAlumnoNotaMayor} con la nota {notaMayor} fue la mas alta");
print(f"el promedio de notas fue de {sumaNotas/cantAlumnos}");