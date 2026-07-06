"""""
LISTAS NUMERICAS: 
1. Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros: 
[1,2,3,4,5,6,7,8,9,10]. 
2. Crea una nueva lista con los números pares de la lista anterior en orden inverso 
3. Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por 
consola.  
4. Intenta rehacer los pasos 2 y 3  con el menor número de lineas posible (método de 
compresión).  
5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla 
6. Haz lo mismo con el número más alto 
7. Suma todos los elementos de la lista con y sin un bucle.  
8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras 
el punto 2. 
"""
#1
numeros=list(range(1,11))
print(numeros)
#2
list_pares_inverso=[]
 
for num in numeros:
    if num%2==0:
     list_pares_inverso.append(num)

for num in list_pares_inverso[::-1]:
     print(num)  

#3
for num in numeros:
   cuadrado_num=num**2
   print(f"el cuadrado de {num} es : {cuadrado_num}") 

#4
   print(min(numeros))  
   print(max(numeros))  

#5
suma=0
#for i in range(11):
   #suma+=i

#print(suma)   

#for num in numeros:
   #suma+=num

#print(suma)   
#
suma=sum(numeros)
print(suma)

#8
for i in range(len(numeros)):
   if numeros[i]==8:
    print(i)
#
for i in range(len(list_pares_inverso)):
   if list_pares_inverso[i]==8:
    print(i)
