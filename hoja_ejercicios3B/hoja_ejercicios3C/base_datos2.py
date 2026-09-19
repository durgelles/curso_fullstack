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
estudiantes= [  ["pedro",[8,7,9]],["ruben",[9,10,9]],["dennis",[6,7,8]]]
all_notas=[]
#recorres la lista de estudiantes
for dato in estudiantes:
    nombres=dato[0]
    notas=dato[1]
    media_notas=sum(notas) / len(notas)
    all_notas.append(media_notas)
    media_total=sum(all_notas) / len(all_notas)
    print(f"las notas  de {nombres} es : {notas} y su promedio es de {media_notas}")


        
    

 
print(f" el promedio general de los alumnos es : {media_total:.2f}") 
     
   

 