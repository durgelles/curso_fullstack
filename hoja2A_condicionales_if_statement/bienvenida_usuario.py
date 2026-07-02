"""""
BIENVENIDA AL USUARIO:
Un ordenador tiene tres usuarios distintos (Alejandro, Naomi y Sergio) y otro usuario invitado. 
Haz un script que pida el nombre al usuario y le dé una bienvenida personalizada. Crea el script 
de tal manera que si el usuario no es ninguno de los tres se le dé un saludo genérico.
¿Que ocurre si uno de los usuarios introduce su nombre completamente en minúsculas?¿Y si lo 
introduce en mayúsculas? ¿Y si sin querer pone in punto en mitad de su nombre (p.e. nao.mi)?¿Y 
si se le cuela una almohadilla (p.e se#rgio)?
"""
#pedir nombre del usuario
nombre_usuario=input(" Ingrese su nombre : ")
nombre_usuario=nombre_usuario.replace(".","")
nombre_usuario=nombre_usuario.replace("#","").lower()

#logica de comparacion
if nombre_usuario=="alejandro" or nombre_usuario=="naomi" or nombre_usuario=="sergio":
    print(f"Bienvenido {nombre_usuario.title()}")
else:
    print("hola, ah iniciado la sesion de invitado")


