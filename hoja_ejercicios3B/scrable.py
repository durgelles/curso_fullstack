""""SCRABBLE:
Supongamos una lista de de caracteres llamada “palabras“ que representa una mano de
Scrabble. Cada string contiene dos caracteres: el primer carácter es la letra de una ficha y el
segundo el numero que representa los puntos de la ficha. Por ejemplo, el string "A5" representa la
ficha con la letra A y un valor de 5 puntos. Crea un script que calcule el valor total de los puntos
en una mano de scrabble. El valor total será la suma de los puntos de todas las fichas de la mano.  """

#crear lisata de caracteres
palabra=["A1","B3","H4","D2","R1","E1","M3"]
valores=[]
#recorrer lista
for ficha in palabra:
    for caracter in ficha:
        if caracter.isdigit():
            valores.append(int(caracter))


print(sum(valores))          


