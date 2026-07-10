"""""3. Escribe un script que encuentre el segundo número más grande de una lista."""""
#crear lista
list=[23,45,55,12,2,78,95,4,29]
list.sort()
mayor=list[0]
print(list)
print(list[-2])

for num in list:
    if num>mayor:
        mayor=num
       
