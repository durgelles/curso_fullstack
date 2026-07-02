"""""DIVISION:
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el 
divisor es cero el programa debe mostrar un error.
"""
#pedir numeros al usuario
num1=float(input("ingrese el primer numero "))
num2=float(input("ingrese el segundo numero "))

if num2 == 0 :
    print("el divisor es cero no se posible la division")
else:
    divison_resultado=num1/num2

    print(f"el resultado de la division entre {num1} y {num2} es {divison_resultado}")