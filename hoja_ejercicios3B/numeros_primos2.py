""""Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con
los números primos de la lista original. Además, el script debe devolver el número total de
números primos encontrados y la suma de los números primos encontrados"""
#crear lista de numeros enteros 
numeros=[1,2,6,5,7,9,32,12,56,29]
lista_primos=[]
total_primos=0
suma_primos=0
#recorrer la lista de numero 
for number in numeros:
    primos=True
    for i in range(2,number):
        if number%i ==0:
            primos=False

    if primos:
        lista_primos.append(number)    
        suma_primos = sum(lista_primos)


print(lista_primos)
print(f"la suma de  los numeros primos es {suma_primos}")
print(f"la cantidad de numero primos es {len(lista_primos)}")
