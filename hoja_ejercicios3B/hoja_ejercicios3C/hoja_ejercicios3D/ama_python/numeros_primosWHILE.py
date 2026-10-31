#crear un scrip que imprima todos los numeros primos hasta el 100
#crear variable boleana


for num in range(2,101):
    primo=True
    i=2
    while primo==True and i < num:
        if num%i==0:
            primo=False

        i+=1

    if primo==True:
        print(num)

         