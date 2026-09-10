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
estudiantes= [  ["pedro",8,7,9],["ruben",9,10,9],["dennis",6,7,8],["ana",9,8,10],["karla",10,9,7]]
#crear lista de materias
materias=["deberes","examenes","proyectos"]
lista_notas=[]
#recorres listas
for i in range(len(estudiantes)):
    suma=0
    for j in range(1,len(estudiantes[i])):
        suma+=estudiantes[i][j]
        lista_notas.append(estudiantes[i][j])
        

    print(f" la nota media del estudiante  {estudiantes[i][0]} es {suma/3}")


print(f" el promedio de la clase es : {sum(lista_notas)/len(lista_notas)}")


     