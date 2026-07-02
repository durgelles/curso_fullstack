"""""
Para tributar en un determinado país es necesario ser mayor de edad y cobrar más de 1000 euros 
al mes. Además los tramos impositivos de la renta anual son los siguientes:
RENTA                     TIPO IMPOSITIVO
Menos de 15.000 eu           5%
Entre 15.000 y 25.000 eu     15%
Entre 25.000 y 35.000 eu     20%
Entre 35.000 y 60.000 eu     30%
Más de 60.000 eu             45%

Escribe un script que primero compruebe si eres susceptible de que se te aplique algún tipo 
impositivo y en caso afirmativo imprima por pantalla cuál te tocaría.
"""
#preguntar si cumple con las condiciones para tributar 
edad=int(input("ingrese su edad "))
ingresos=float(input("introduzca sus ingresos mensuales "))
renta=float(input("ingrese su cuanto paga de renta: "))

#logica
cant_impositivo=0
if edad >= 18 and ingresos > 1000:
    if renta <= 15000 :
        cant_impositivo=renta*0.05
        print(f" se te cobrara un impositivo de 5% la cantidad es de {cant_impositivo} ")
    elif  renta <= 25000:
        cant_impositivo=renta*0.15
        print(f" se te cobrara un impositivo de 15% la cantidad es de {cant_impositivo} ")
    elif  renta <= 35000:
        cant_impositivo=renta*0.20
        print(f" se te cobrara un impositivo de 20% la cantidad es de {cant_impositivo} ")
    elif  renta <= 60000:
        cant_impositivo=renta*0.30
        print(f" se te cobrara un impositivo de 30% la cantidad es de {cant_impositivo} ")
    else:
        cant_impositivo=renta*0.45
        print(f" se te cobrara un impositivo de 45% la cantidad es de {cant_impositivo} ")
else:
     print("no cumple con los parametros parametros para pagar impositivo")