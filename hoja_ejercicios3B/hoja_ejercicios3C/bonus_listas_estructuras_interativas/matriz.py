"""MATRIZ:
Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en
ese caso imprima dos listas correspondientes a:
1. La fila cuyos elementos suman el máximo
2. La columna cuyos elementos suman el máximo
Si no se trata de una matriz devolverá dos listas vacías.
Por ejemplo:
M1=[[2,5,3],[6,1,8],[7,5,4]] devolverá: L1 = [7,5,4] y L2 = [2,6,9,7]
M2 = [[4,2,3],[4,5],[6,8,2]] devolverá: L1 = [] y L2 = []
(Nota: Definimos matriz como una lista de listas donde todas las listas internas tienen el mismo
numero de objetos) """

#se crea una lista
M1= [[2,5,3],
     [6,1,8],
     [7,5,4]]
#se crean dos listas vacias para almacenar las sumas de las columnas y las filas
suma_filas=[]
suma_columnas=[]
columnas = []
lista_fila_mayor=[]
lista_columna_mayor=[]
# se extrae el tamaño de la primera sublista para comparar 
tam=len(M1[0])
# se recorre la lista y se comparan las sublistas a ver si es una matriz
matriz=True
for list in M1:
   
   if len(list)!=tam:#se compara el tamaño de cada fila si es desigual no es matriz
      matriz=False
      break
    #se suman las filas
   suma_filas.append(sum(list))


   
# se verifica si es una matriz
if matriz==True:#boleano para mostrar las opciones
   print("la lista es una matriz")
   #recorrer lista y encontra el mayor fila
   mayor_fila=max(suma_filas)
   for i in range(len(suma_filas)):
       
        #determinar su indice
       if mayor_fila==suma_filas[i]:
         ind=i  
         lista_fila_mayor.append(M1[ind])  
         print(f"la fila que mayor suma tienes es {M1[ind]} y y su suma es de {mayor_fila}")
         print(f"la lista de la fila mayor es {lista_fila_mayor}")
  
  
  #buscar la columna con mayor
  # se crea los espacios de las sublistas de columnas y se recore las columnas
   for j in range(len(M1[0])):
      columnas.append([])
      #se recorre las filas hacia abajo por cada columna(j)
      for i in range(len(M1)):
         columnas[j].append(M1[i][j])
         

   for adition in columnas:
     suma_columnas.append(sum(adition))
  
  
   mayor_columna=max(suma_columnas)
   for i in range(len(columnas)):
     if mayor_columna==suma_columnas[i]:
        lista_columna_mayor.append(columnas[i])
        print(f" la columna que mayor suma tienen es {columnas[i]} y su suma es de {mayor_columna}")
        print(f"la lista de la columna mayor es {lista_columna_mayor}")


else:
   print("la lista no es una matriz")
   

  

   