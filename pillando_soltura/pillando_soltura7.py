"""""7. Crea un script que extraiga los elementos comunes entre dos listas."""
#creando las listas
list1=[1,34,54,8,6,55,90,54,23,6,4,]
list2=[2,66,54,89,54,80,8,34,12,10]
elementos_comunes=[]
#comparando las listas
for i in list1:
    for j in list2:
       if i==j and i not in elementos_comunes:

        elementos_comunes.append(i)

print(elementos_comunes)       