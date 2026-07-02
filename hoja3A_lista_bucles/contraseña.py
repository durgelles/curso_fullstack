"""""

2. Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. 
"""
#guardando contrasela correcta 
contraseña_correcta="123"
pass_tru= False

#preguntar contraseña al usuario hasta que sea la correcta
while pass_tru==False:
    password=input("ingrese la contraseña : ")
    if password==contraseña_correcta:
        pass_tru=True
        print("contraseña correcta bienvenido")
    else:
        print("contraseña incorrecta")





