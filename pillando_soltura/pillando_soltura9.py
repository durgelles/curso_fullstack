"""""9. Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo 
números positivos de la lista original. """
#crear lista 
lista_enteros=[3,9,8,89,78,-7,45,-41,12,64,-52]
lista_positivos=[]
#recorrer lista de 
print(lista_enteros)
for num in lista_enteros :
    if num > 0 :
     lista_positivos.append(num)
     

print("la lista con numeros positivos es : ")
print(lista_positivos)  

