"""""
TARJETA DE CRÉDITO: 
Crea un script que reciba como input un número de tarjeta de crédito e imprima por pantalla todos 
los caracteres en forma de asterisco salvo los últimos cuatro. Si por ejemplo el número de tarjeta 
es 1234 2345 3456 5678, el output deberá ser **** **** **** 5678.
"""
#pedir el numero de la targeta
numero_tarjeta=input("ingrese el numero de la tarjeta")
longitud=len(numero_tarjeta)

print("*" * (longitud-4)+(numero_tarjeta[longitud-4:longitud]))