"""""
BECAS PARA ESTUDIANTES (BONUS*):
El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media. 
Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. Crea un script que 
pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no.
*Los ejercicios bonus no se resolverán directamente en clase si no que están pensados para que 
los alumnos los discutan por el chat de Discord y compartan sus soluciones. Las soluciones 
compartidas de los alumnos se subirán en un archivo a la academia.
"""
#se pide el nombre , la edad y lanota media
nombre=input("ingrese su nombre :  " )
edad=int(input("ingrese au edad : "))
nota_media=float(input("ingrese su nota media : "))

#logica 

if 17<=edad<=21 and nota_media>=8:
    print(f"felicidades {nombre},puedes optar por la beca")
else:
    print(f"no cumple con los parametros para optar por la beca")