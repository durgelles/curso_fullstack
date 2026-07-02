"""""
REORDENANDO NUMEROS:
a. Crea un script en el que el usuario introduzca un número de más de una cifra. El script debe 
imprimir los componentes del número uno a uno por pantalla. Por ejemplo si el número introducido 
es el 4532 por pantalla deberá imprimirse:
4
5
3
2
b. Crea un script que dado un numero entero de cuatro cifras calcula e imprima el número que 
resulta de leer el número introducido de derecha a izquierda. Por ejemplo si el número introducido 
es 4532, el output deberá ser 2354.
"""

#pedir numero al usuario
numero = input("ingrese un numero de cuatro cifras " )

print(numero[0]+"\n"+numero[1]+"\n"+numero[2]+"\n"+numero[3])

#imprimirlo al reves
print(numero[::-1])