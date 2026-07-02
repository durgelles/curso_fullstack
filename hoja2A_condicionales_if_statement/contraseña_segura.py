"""""
CONTRASEÑA SEGURA:
Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos 
especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario, 
comprueba si es una contraseña segura e indícalo por pantalla.
"""
#pedir contraseña al usuario
contraseña_usuario = input("ingrese su contraseña para verificar : ")


if ("#" in contraseña_usuario or "*" in contraseña_usuario) and ("a" in contraseña_usuario or "e" in contraseña_usuario or "o" in contraseña_usuario ):
    print("la contraseña es segura")
else:
       print("la contraseña no es segura")     