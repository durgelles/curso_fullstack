#crear un scrip que imprima todos los numeros primos hasta el 100
#crear variable boleana


for num in range(2,101):
    primo=True
    for i in range(2,num):
        if num % i ==0:
            primo=False
            break


    if primo==True:
     print(num)