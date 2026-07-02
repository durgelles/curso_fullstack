""""
EL MAYOR DE CUATRO:
Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por 
pantalla.
"""
numeros=[]
#pedir numeros al usuario
for i in range(4):
    numero=int(input(f"ingrese un numero {i+1} : "))
    numeros.append(numero)



print(numeros)

numero_mayor=numeros[0]

for num in numeros:
    if num > numero_mayor:
        num=numero_mayor

print(f"el numero mayor de la lisa es {numero_mayor}")