"""PALABRAS PROHIBIDAS:
Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras.
Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga
aquellas palabras que no tienen ninguna letra prohibida. """
#crear listas
lista_palabras_aleatorias=["mesa","ventana","cocina","cama","baño"]
letras_prohibidas=["i","o","u"]
palabras_filtradas=[]

for i in letras_prohibidas:
    for j in lista_palabras_aleatorias:
        if i not in j and j not in palabras_filtradas :
            palabras_filtradas.append(j)


print(palabras_filtradas)
