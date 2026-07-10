"""""4. Crea un script que cuente el número de elementos más grandes que un determinado número 
dado por el usuario (supón una lista numérica).""""" 
#crear lista y contador
list=[32,34,56,43,12,66,74,33,1,29,30]
numeros_mayores=[]
cont=0
#pedir numero al usuario
numero_usuario=int(input("ingrese un numero : "))
print(list)
for num in list:

    if num > numero_usuario:
        cont+=1
        numeros_mayores.append(num)

print(f"la lista tiene {cont} numeros mayores que {numero_usuario} y son :")
print(numeros_mayores)

