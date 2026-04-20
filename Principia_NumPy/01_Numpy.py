# numpy
sep = "=" * 123
#* pip install numpy instala la libreria

import numpy as np #* Importo la libreria y la renombro como np

lista = [1, 2, 3, 4, 5] #lista normal
arr = np.array([1, 2, 3, 4, 5]) #lista arreglada (ya una matriz)

print(type(arr)) #<class 'numpy.ndarray'>

print(lista * 2) #! Imprime dos veces la lista
print(arr * 2) #! Multiplica * 2 la lista

arr1 = np.array([1, 2, 3]) #arreglo 1
arr2 = np.array([4, 5, 6]) #arreglo 2

print(arr1 + arr2) #Suma los arreglos (suma de matrices) #? Anteriormente tenia la duda de como podria sumar vectores y ya estaba pensando en un codigo, pero con esto es super facil
print(arr1 * arr2) #Multiplicación de acuerdo a la posicion #? No estoy tan seguro que realmente sea multiplicación de matrices, deberia de comprobarlo para un 3x3 y tal vez asi podria saber si efectivamente es


A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])


print(A * B)    #! elemento por elemento
print(A @ B)    #! multiplicación matricial real 
#TODO PENDIENTE : "implementar multiplicación matricial desde cero"

print(sep)

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matriz.shape) #! Devuelve la dimensiones de la matriz (arreglo)
print(matriz.T) #! Devuelve la transpuesta

x = np.linspace(0, 10, 100) #! x = np.linspace(0, 10, 100)

print(x)    

x = np.linspace(0, 10, 100)
y = x**2

print(y)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = x**2

plt.plot(x, y)
plt.show()

print(sep)

lista_Numeros = [[2, 3, 4],
                 [3, 4, 5],
                 [2, 5, 1],
                 [5, 8,10]]

arr_numeros = np.array(lista_Numeros)
print(arr_numeros)

print(arr_numeros.shape) #* Tamaño de mi arreglo (Matriz_mxn) (Renglones, Columnas)

print(arr_numeros.ndim) #! No son como las dimensiones normales en A.L

print(sep)

#* Como funciona:
# 1D — necesitas 1 índice
#arr[2]

# 2D — necesitas 2 índices  
#arr[1][2]  # fila 1, columna 2

# 3D — necesitas 3 índices
#arr[0][1][2]  # "capa" 0, fila 1, columna 2

# 3 instantes de tiempo, cada uno con matriz 4x3
Matriz3D = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
                  [[2,3,4],[5,6,7],[8,9,10],[11,12,13]],
                  [[3,4,5],[6,7,8],[9,10,11],[12,13,14]]])

print(Matriz3D.shape)  # (3, 4, 3) #(capas, filas, columnas)
print(Matriz3D.ndim)   # 3

# Para 1 de 4 # (bloques, capas, filas, columnas)

print(Matriz3D.dtype) #int 64, enteros de 64bits

print(Matriz3D.size) #32, 32 datos

#Matriz3D = np.array(Matriz3D, dtype = np.int16) #Limita a 16bits
#print(Matriz3D) 


print(np.zeros((3, 2))) #* Matriz de 0, (3 Renglones,2 Columnas)

print(np.ones((5,7))) #* Matriz de 1, (5 Renglones,7 Columnas)

print(np.empty((2,3))) #Numeros muyyy pequeños, pero no 0 (2 Renglones,3 Columnas)

print(np.arange(10)) #Py es de indice 0, comienza en 0 hasta 9 en este caso
print(np.arange(10).reshape(2, 5)) # La misma matriz, pero en 2 filas y 5 columnas

print(np.arange(10, 20, 2)) #Le que ahora inicie en 10, termine en 20, en saltos de 2 en 2, no incluye el 20 por lo mismo del indice 0
#! Si quieisera el 20, tendria que pedirle hasta el 21

print(np.linspace(10, 20, 20)) #Numeros espaciados de 10 al 20, con espacios divididos equitativamente 20 veces

print(sep)

from numpy import pi
print(pi)

rad = np.linspace(0, 2 * pi, 100) #Del 0 a 2pi, espaciados en 100 numeros

print(rad)

sen = np.sin(rad)
print(sen)
cos = np.cos(rad)
print(cos)

import numpy as np #! Importar las dependencias
import matplotlib.pyplot as plt

plt.plot(sen, cos)
plt.show()


plt.plot(rad, sen)
plt.plot(rad, cos)
plt.show()

print(sep)

a = np.linspace(10, 20, 6)
b = np.linspace(5, 25, 6)
print(a, b) #Me da las dos arreglos a y b, solo los da no hace nada más

#Operaciones con arreglos

print(a + b) #Suma los arreglos

c = np.concatenate((a,b))
print(c) #Los junta (Concatena)

c.sort()
print(c) #Los ordena de menor a mayor

print(sep)

#rg (radom generator)

rg = np.random.default_rng(2) #generador de numeros, pero con semilla 2, es "radom", pero con una semilla especifica por lo que son los mismos datos si lo dejara sin ninguna semilla pues seria totalmente radom, ahi lo que pasa es que no hay reproducibilidad de los datos, para eso sirve la semilla
aleatorio = rg.random(1000)
print(aleatorio)
plt.hist(aleatorio, bins = 100)
plt.show()

normal = rg.normal(10, 5, 100000) #Con los datos de aleatorio quiero utilizando la funcion normal, con media 10 con desvest de 5 me de 100000
print(normal) #muestra primeros 3 y ultimos 3
plt.hist(normal, bins = 1000)
plt.show()

enteros = rg.integers(20, size = 2000) #Enteros
plt.hist(enteros)
plt.show()

sin_repetir = rg.choice(26, size = 10, replace = False) #Numero aleatorios sin repetir
print(sin_repetir)

estadistacos = rg.integers(20, size = 8)
print(estadistacos.min()) #El minimo
print(estadistacos.max()) #El maximo
print(estadistacos.mean()) #La media
print(estadistacos.std()) #La dvst
print(estadistacos.sum()) #La suma
print(estadistacos)

estadistacos_2D = rg.integers(20, size = (5,4))
print(estadistacos_2D)
print(estadistacos_2D.min(axis = 0)) #! axis = 0, que trabaje a lo largo de las columnas, (COLUMNAS)
print(estadistacos_2D.max(axis = 1)) #! axis = 1, que trabaje a lo largo de las filas, (FILAS)

print(estadistacos_2D[estadistacos_2D < 12]) #Arreglo con solo mis numeros menores a 12, pierde la forma del arreglo, pero hace un nuevo arreglo con solo numeros menores a 12

print(sep)

np1 = rg.integers(20, size=(3,3))
np2 = rg.integers(20, size=(3,3))
np.vstack((np1, np2))
print(np1, "\n\n", np2)

print(np.vstack((np1, np2)))
print(np.vstack((np1, np2))) #Apilamiento vertical
print(np.hstack((np1, np2))) #Apilamiento horizontal

enteros_2 = rg.integers(20, size=(10))
print(enteros_2)

print(enteros_2[0:6]) #Me da los primeros 6 valores del arreglo

print(enteros_2[0:6:2]) #Que seleccione los primeros 6 valores del arreglo de dos en dos
print(enteros_2[::2]) #Que inicie y termine desde que comienza, hasta que termina, pero de dos en dos

enteros_2D = rg.integers(20, size=(8,5))
print(enteros_2D)

print(enteros_2D[1, 3]) #Me da del segundo Renglon el cuarto valor, #! Aqui tambien aplica el indice 0, es decir no es primer renglon es segundo el primero seria 0

print(enteros_2D[3:6, 1]) #! De la fila del 3 al 5, es decir, 3, 4, 5 agarra los valores de la columna 2

print(enteros_2D[4:7,0:2]) #! De la fila 4 a la 6, es decir, 4, 5, 6, agarra los valores de sus columnas 1 y 2