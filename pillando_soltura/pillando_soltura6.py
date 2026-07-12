"""""6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto 
que es inferior al número introducido o determinado al inicio del programa"""""
#pedir numero al usuario
numero_usuario=int(input("ingrese un numero : "))
#crear lista del 1 al 100
lista_numeros=list(range(1,101))
numero_inferior=None
#recorrer lista de numeros para determinar el antecesor 
for i in range(1,101):
    if i < numero_usuario:
        
        numero_inferior=i

print(numero_inferior)        