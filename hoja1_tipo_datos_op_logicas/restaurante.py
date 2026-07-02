"""""
RESTAURANTE:
En un restaurante el menú consta de las siguientes opciones:
Ensalada mixta   ————————   12 EU
Sopa de pescado    ———————   10 EU
Dorada al horno  ————————   18 EU
Arroz al curry  —————————   14 EU
Lasaña de carne     ———————   15 EU
Brownie de chocolate    —————    8 EU
Helado    ———————————    6 EU
Refrescos    ——————————    5,5 EU
Café    ————————————    3,5 EU
Escribe un script que lea la cantidad de cada alimento consumido y que calcule e imprima el total 
de la cuenta.
"""
#se declara el valor a las variables 
ensalada_mixta=12
sopa_pescado= 10
dorada_horno=18
arroz_curry=14
lasaña_carne=15
brownie_chocolate=8
helado=6
refrescos=5.5
cafe=3.5
#preguntar nombre 
nombre=input("hola , cual es su nombre ")
print(f"{nombre} , necesitamos saber la cantidad que consumio de cada oferta del menu")
#guardar la cantidad consumida por el usuario
cant_ensalada_mixta=int(input("que cantidad de ensalado mixta consumio " ))
cant_sopa_pescado=int(input("que cantidad de sopa de pescado consumio "))
cant_dorada_horno=int(input("que cantidad de dorada al horno consumio "))
cant_arroz_curry=int(input("que cantidad de arroz al curry consumio "))
cant_lasaña_carne=int(input("que cantida de lasaña de carne consumio "))
cant_brownie_chocolate=int(input("que cantida de brownie de chocolata consumio "))
cant_helado=int(input("que cantida de helado consumio "))
cant_refrescos=int(input("que cantida de refrescos consumio "))
cant_cafe=int(input("que cantida de cafe consumio "))
total_cuenta=ensalada_mixta*cant_ensalada_mixta+sopa_pescado*cant_sopa_pescado+dorada_horno*cant_dorada_horno+\
arroz_curry*cant_arroz_curry+lasaña_carne*cant_lasaña_carne+brownie_chocolate*cant_brownie_chocolate+\
helado*cant_helado+refrescos*cant_refrescos+cafe*cant_cafe
print(f"la cuenta total es de {total_cuenta}")



