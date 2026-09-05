"""" EL COMERCIAL:
Eres un comercial trabajando para una compañía que vende diversos productos. Quieres crear un
programa para realizar un seguimiento de los productos que has vendido y el valor total de las
ventas. Supongamos que hay un total de 10 productos.
Tú has vendido 5 de estos productos en las siguientes cantidades:
Producto 1: 3 unidades
Producto 2: 1 unidad
Producto 5: 7 unidades
Producto 6: 2 unidades
Producto 9 : 4 unidades
Los precios de cada uno de estos productos son como siguen:
Producto 1: 30.0 EU		 Producto 6: 44.0 EU
Producto 2: 9.8 EU		 Producto 7: 21.2 EU
Producto 3: 42.5 EU		 Producto 8: 53.2 EU
Producto 4: 32.6 EU		 Producto 9: 25.3 EU
Producto 5: 71.5 EU		 Producto 10: 57.8 EU
Crea un script que dada una lista con los productos, sus precios y las unidades vendidas, imprima
la cantidad total de ventas, el dinero facturado por producto y el dinero total. """
#darle bienbenida al usuario
nombre=input("hola, ingrese su nombre :")
print(f"hola {nombre} a continuacion le mostramos la lista de productos con el precio:")


#creando listas 
lista_productos=["producto1","producto2","producto3","producto4","producto5","producto6","producto7","producto8","producto9","producto10"]
lista_precios=[30.0, 9.8, 42.5, 32.6, 71.5, 44.0, 21.2, 53.2, 25.3, 57.8]
unidades = [3, 1, 0, 0, 7, 2, 0, 0, 4, 0]
dinero_x_producto=[0,0,0,0,0,0,0,0,0,0]
cantidad_total_ventas=0

"""for i in range(5):
    print(f"{lista_productos[i]}: {lista_precios[i]} EU     {lista_productos[i + 5]}: {lista_precios[i + 5]} EU")

for i in range(len(unidades)):
    if unidades[i] != 0:
        dinero_x_producto[i]=unidades[i]*lista_precios[i]
        cantidad_total_ventas+=unidades[i]

print(dinero_x_producto)
print(cantidad_total_ventas)  

print(f"el monto de dinero por producto es : ")
for i in range(5):
    print(f"{lista_productos[i]} , {unidades[i]} unidades: {dinero_x_producto[i]} $ EU     {lista_productos[i + 5]} , {unidades[i]} unidades : {dinero_x_producto[i + 5]} $ EU")

print(f"la cantidad de productos vendidos es de {cantidad_total_ventas}")    

print(f"el total de dinero recaudado en la venta de todos los productos es {sum(dinero_x_producto)}")""" 



for i in range(len(lista_precios)):
    dinero_x_producto=lista_precios[i]*unidades[i]
    print(f"el dinero facturado por el producto{i+1} es {dinero_x_producto}")