"""""
EL TRIÁNGULO:
En una obra es necesario construir para el tejado de una casa una estructura triangular con tres 
piezas. El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir 
este estructura. Crea un script que dados tres longitudes indique si podría construirse un triangulo 
con esas piezas.
(Pista: la suma de dos piezas tiene que ser mayor que el lado restante. Esto debe ser así para 
todas las posibles combinaciones)
"""
#pedir la largura de los lados
lado_1=int(input("ingrese el largo del lado : "))
lado_2=int(input("ingrese el largo del lado : "))
lado_3=int(input("ingrese el largo del lado : "))
#logica

if (lado_1+lado_2>lado_3) and (lado_1+lado_3>lado_2) and (lado_3+lado_2>lado_1):
    print("si se forma un triangulo con esas medidas ")
else:
    print(("no se forma un triangulo con esas medidas "))
