"""""
CASA DE CAMBIOS: 
Una casa de cambios necesita construir un programa que dada una cantidad de euros introducida 
por el usuario de el resultante en dólares. 
1. Crea un script que reciba una cantidad de euros del usuario e imprima por pantalla el 
correspondiente en dólares (considera una tasa de cambio donde 1 EU = 1.2 $)
2. La casa de cambios se queda un 10% en concepto de ‘tasas de gestión’. Calcula el monto 
recibido, el cambio en dólares, la cantidad que se queda la casa de cambios y la cantidad de 
dólares restante que recibirá el usuario. Imprime el desglose por pantalla formateado de tal 
forma que quede claro para el usuario. 
"""

#pedir al usario que ingrese la cantidad a cambiar en euros 
euros_usuario=float(input(f"ingrese la cantidad de euros a cambiar : "))
#calcular cuanto es en dolares
dollars=euros_usuario*1.2
#calcular la tasa de gestion
tasa_gestion=dollars*0.10
#dolares recibidos por el usario
dollars_usuario=dollars-tasa_gestion

print(f"el cambio de {euros_usuario} euros es {dollars} dolares")
print(f"la tasa de gestion de cambio es del 10 % y es de {tasa_gestion} dolares")
print(f"recibe {dollars_usuario} dolares")
print("gracias por utilizar nuetros servicios vuelva pronto")