"""""1. Escribe un programa en Python para encontrar los elementos duplicados de una lista, 
añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los 
elementos únicos. """""
#crear listas
lista=[2,3,4,4,5,6,7,8,3,2,8,10]
lista_duplicados=[]
unicos=[]

#recorrer lista
for num in lista:
    if lista.count(num)==1:
       unicos.append(num)
else:
   lista_duplicados.append(num)

#mostrar resultados
print("lista de numeros: ")
print(lista)
print(f"lista de numeros duplicados : ")
print(lista_duplicados)
print("lista de numeros unicos : ")
print(unicos)
    


