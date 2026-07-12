"""""8. Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista 
(P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2) """""
#crear lista c
lista=[2,45,65,3,4,22,5,6,56,65,78,45,4,3,65]
cont=0
#mostrando lista
print(lista)
# pedir al usuario 
numero_usuario=int(input(" escoja un de la lisa para saber cuantas veces se repite : "))

#recorrer lisa
if numero_usuario in lista:
  
  for num in lista:
     if num==numero_usuario:
      cont+=1

else:
  print("el numero no aparece en la lista")


if cont > 1:
   print(f"el numero {numero_usuario} se repite en la lista {cont} veces")
elif  cont==1:
   print(" el numero solo aparece una vez")

      