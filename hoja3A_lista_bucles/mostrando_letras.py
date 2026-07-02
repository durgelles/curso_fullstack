"""""
3. Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras 
de la palabra introducida empezando por la última. 
"""
#pedir palabra al usuario 
palabra = input("ingrese una palabra : ")
# recorrer la palabra e imprimir letra a letra
for i in(palabra)[::-1]:
    print(i)