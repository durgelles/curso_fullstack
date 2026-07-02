"""""
PAR O IMPAR: 
Crea un script que dado un número y una potencia compruebe si ese numero elevado a esa 
potencia es par o impar. (Pista: los números pares tiene resto = 0 al dividirlos por 2)
"""
#pedir al usuario un numero y la potencia a la cual se va a elevar
numero=int(input("ingrese el numero que desea: "))
potencia=int(input("ingrese la potencia a la que desea elevar el numero: "))
#calculo de la potencia
resultado=numero**potencia
#logica para saber si es par o impar
if resultado%2==0:
    print(f"el resultado {resultado} es par") 
else:
    print(f"el resultado {resultado} es impar")
