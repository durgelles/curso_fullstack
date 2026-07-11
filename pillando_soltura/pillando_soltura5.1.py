"""""5. Crea un script dado un número introducido por el usuario o determinado al inicio del 
programa, realice la suma de aquellos números que sean divisibles por este. """""
#pedir un numero al usaario:
numero_usuario=int(input("ingrese un numero: "))
# realizar lista hasta el 100 para ver los numeros divisibles
numeros=list(range(1,numero_usuario+1))
lista_divisible=[]
#recorrer la lista de los numeros 
print(f"los numeros divisibles por {numero_usuario} son :")
for num in numeros:
    if numero_usuario%num==0:
        lista_divisible.append(num)
        print(num)  

suma_de_divisibles=sum(lista_divisible)
print(f"la suma de los numeros divisibles del {numero_usuario} es: {suma_de_divisibles}")