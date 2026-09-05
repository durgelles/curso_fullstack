""""BASE DE DATOS DE UN COLEGIO:
Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los
estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
También necesitas calcular a nota media de cada estudiante y la nota media de la clase al
completo.
Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para
cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota
media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la
clase. """

#crear lista de nombre de estudiantes con las notas
estudiantes=[["pedro",8,7,9]],["ruben",9,10,9],["dennis",6,7,8],["ana",9,8,10],["karla",10,9,7]
#crear lista de materias
materias=["deberes","examenes","proyectos"]
#recorres listas
for i in range(len(estudiantes)):
    for j in range(len(materias)):
        print(f"estudiante {estudiantes[i][0]} , en la materia {materias[2]} su nota fue de {estudiantes[i][j+2]}")
