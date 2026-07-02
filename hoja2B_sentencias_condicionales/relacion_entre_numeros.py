"""""
RELACION ENTRE NÚMEROS:
Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma 
de los otros dos. 
"""
# pedir numeros al usuario
numeros=[]

for i in range(3):
    numero=int(input(f"ingrese el numero {i+1} : "))
    numeros.append(numero)

print(numeros)

if numeros[0]==numeros[1]+numeros[2]:
   print(f"el numero {numeros[0]} es la suma de los numeros {numeros[1]} y {numeros[2]} " )
elif numeros[1]==numeros[0]+numeros[2]:
   print(f"el numero {numeros[1]} es la suma de los numeros {numeros[0]} y {numeros[2]} " )
elif numeros[2]==numeros[1]+numeros[0]:
   print(f"el numero {numeros[2]} es la suma de los numeros {numeros[1]} y {numeros[0]} " )
else:
   print("ningun numero coincide la suma de los otros dos")

   

