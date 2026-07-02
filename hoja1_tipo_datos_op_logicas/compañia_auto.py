"""""
COMPAÑÍA DE AUTOMÓVILES:
Una compañía de automóviles vende tres tipos de coche: RBM Serie 1, RMB Serie plus, RBM 
todoterreno. Cada uno de estos coches tiene un precio de venta y el vendedor recibe una 
comisión diferente por cada tipo de coche que ha vendido.
Suponga que los precios y las comisiones son:
RBM Serie 1: 
precio: 20.000 EU, comisión: 3%
RMB Serie plus: 
precio: 35.000 EU, comisión: 5%
RBM todoterreno: 
precio: 60.000 EU, comisión: 7%
Crea un programa donde el usuario introduzca el numero de coches vendidos de cada tipo ese 
mes  y que le devuelva la cantidad en euros a comisionar ese mes.
"""
#preguntar al usuario la cantidad de coches vendidos

coches_RMB_serie1=int(input("Cuantos autos vendio del RMB serie 1 este mes "))
coches_RMB_serie_plus=int(input("Cuantos autos vendio del RMB serie plus este mes "))
coches_RMB_serie_todoterreno=int(input("Cuantos autos vendio del RMB serie todoterreno este mes "))

#guardar variables con los datos
precio_RMB_serie1=20000
precio_RMB_serie_plus=35000
precio_RMB_serie_todoterreno=60000 
comision_RMB_serie1=3
comision_RMB_serie_plus=5 
comision_RMB_serie_todoterreno=7
#calculando la cantidad de comision
cant_dinero_comision_RMB_serie1=precio_RMB_serie1*coches_RMB_serie1* comision_RMB_serie1/100
cant_dinero_comision_RMB_serie_plus=precio_RMB_serie_plus*coches_RMB_serie_plus* comision_RMB_serie_plus/100
cant_dinero_comision_RMB_serie_todoterreno=precio_RMB_serie_todoterreno*coches_RMB_serie_todoterreno* comision_RMB_serie_todoterreno/100
cantidad_total_comision=cant_dinero_comision_RMB_serie1+cant_dinero_comision_RMB_serie_plus+cant_dinero_comision_RMB_serie_todoterreno
#mostrando la respuesta
print(f"se vendieros {coches_RMB_serie1} coches RMB serie 1 este mes y la cantidad a comisionar es de {cant_dinero_comision_RMB_serie1} euros")
print(f"se vendieros {coches_RMB_serie_plus} coches RMB serie plus este mes y la cantidad a comisionar es de {cant_dinero_comision_RMB_serie_plus} euros")
print(f"se vendieros {coches_RMB_serie_todoterreno} coches RMB serie todoterreno este mes y la cantidad a comisionar es de {cant_dinero_comision_RMB_serie_todoterreno} euros")
print(f"en el mes la cantidad de comision que se genero en total fue de {cantidad_total_comision}")