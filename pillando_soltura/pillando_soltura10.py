""""10. Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de 
los strings de la lista original."""
#crear lista
compras_super=["arroz","frijoles","vegetales","carnes"]
tamaño_string=[]
#recorrer le lista
for palabra in compras_super:
    tamaño_string.append(len(palabra))

for i in range(len(compras_super)):
    print(f"la palabra {compras_super[i]} tiene un tamaño de {tamaño_string[i]}")