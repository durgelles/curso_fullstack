"""""
1. Escribe un programa que pida al usuario un número entero y muestre por pantalla una 
estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el 
centro de la estructura. 
* 
** 
*** 
**** 
***** 
**** 
*** 
** 
* 
"""
#pedir un numero entero al usuario
while True:
    try:
        numero=int(input("ingrese un numero entero: "))
        break
    except ValueError:
        print("solo debe ser un numero entero")


for i in range (1,numero+1):
    print("*"*i + " "*(numero-i))

for i in range (numero+1,-1,-1):
    print("*"*i + " "* (numero-i) )