""""LOG-IN:
Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta). 
Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe 
indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la 
contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
Cambia el script para que no distinga entre mayúsculas y minúsculas.
(Pista: Necesitarás in If Statement anidado)
"""
#declarar la contraseña correcta
contraseña_correcta="cr7"

# se le pide al usuario que ingrese una contraseña
contraseña_usuario=input("ingrese la contraseña : ")


if contraseña_usuario==contraseña_correcta:
    print("bienvenido contraseña correcta")
else:
    print("contraseña incorrecta")
    contraseña_usuario=input("ingrese la contraseña : ")
    if contraseña_usuario!=contraseña_correcta:
        print("error , contraseña incorrecta se cerrara el sistema ")
    else:
        print("bienvenido contraseña correcta")

