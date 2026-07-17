""""11. Crea un programa que dada una lista de strings, devuelva otra lista con los strings en 
mayúscula.  """
#crear lista
compras_super=["arroz","frijoles","vegetales","carnes"]
lista_mayusculas=[]
#recorrer le lista
for palabra in compras_super:
    lista_mayusculas.append(palabra.upper())

print(lista_mayusculas)