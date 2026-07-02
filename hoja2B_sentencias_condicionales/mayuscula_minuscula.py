"""""
MAYUSCULA O MINUSCULA (BONUS*):
Permite que el usuario introduzca una letra (del alfabeto latino) como input. Comprueba si esta es 
una mayúscula o una minúscula.
"""
#pedir letra al usario
letra=input("ingrese una letra del alfabeto: ")

#logica 
if letra.isupper():
    print(f"la letra {letra} es mayuscula ")
else:
    print(f"la letra {letra} es minuscula ")

    
