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
#crear lista de notas y nombre de estudiantes
estudiantes= []
all_notes=[]
data_base=[]
#preguntar la cantidad de estudiantes de la base de datos 
cant_student=int(input(" Hola ingrese la cantidad de estudiantes que incluira en la base de datos : "))
#llenar lista con nombre de estudiantes
for i in range(cant_student):
    print("estudiante", i+1)
    nombre=input("ingrese el nombre del estudiante : ")
    estudiantes.append(nombre)

#pedir las notas de las diferentes materias 
#añadirlas a una lista de notas reutilizable para crear la data_base
for estudiante in estudiantes:
    notas=[]
    print(f"ingrese las notas de : {estudiante}")
    deberes=float(input("ingrese la nota de deberes :"))
    notas.append(deberes)
    examenes=float(input("ingrese la nota de examenes :"))
    notas.append(examenes)
    proyectos=float(input("ingrese la nota de proyectos :"))
    notas.append(proyectos)
    data_base.append([estudiante,notas])

print(data_base)



"""
#recorres la lista de estudiantes
for dato in estudiantes:
    nombres=dato[0]
    notas=dato[1]
    media_notas=sum(notas) / len(notas)
    all_notas.append(media_notas)


media_total=sum(all_notas) / len(all_notas)
print(f"las notas  de {nombres} es : {notas} y su promedio es de {media_notas}")
"""""