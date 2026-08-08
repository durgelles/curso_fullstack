"""PALABRAS PROHIBIDAS:
Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras.
Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga
aquellas palabras que no tienen ninguna letra prohibida. """
#crear listas
lista_palabras_aleatorias=["mesa","ventana","cocina","duermo","baño"]
letras_prohibidas=["i","o","u"]
palabras_filtradas=[]


for palabras in lista_palabras_aleatorias:
        incluir=True
        for letra in letras_prohibidas:
            if letra in palabras:
                  incluir=False
        
        if incluir:
            palabras_filtradas.append(palabras)
                       

 
print(palabras_filtradas)