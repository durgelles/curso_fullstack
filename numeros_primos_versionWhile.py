""""
NUMEROS PRIMOS 1: 
Crea un programa que imprima todos los números primos entre el 2 y el 100. Un numero primo es 
un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1 
o sí mismo.
"""
#recorrer los numeros desde 2 hadta el 100
for i in range(2,101):
    primo=True
    j=2
    while primo==True and j < i:
        if i % j == 0:
         primo=False
        j+=1
    
    if primo:
     print(i)            
