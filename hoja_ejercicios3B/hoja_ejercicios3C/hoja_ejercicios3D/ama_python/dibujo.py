#escribir un progama que muestre una estructura
#pedir tamaño de del centro de la estructura al usuario
tam=int(input("ingrese el tamaño de la estructura: "))
#recorrer con un bucle y llenar ascendentemente los espacios
for i in range(tam+1):
    print("*"*i)
for i in range(tam-1,0,-1):
    print("*"*i)
