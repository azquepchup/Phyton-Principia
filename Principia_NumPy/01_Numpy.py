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
print(arr1 * arr2) #Multiplicación de acuerdo a la posicionm #? No estoy tan seguro que realmente sea multiplicación de matrices, deberia de comprobarlo para un 3x3 y tal vez asi podria saber si efectivamente es


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

#Lo dejo en comentario para que no ejecute a cada rato y no llene la terminal

#import numpy as np
#import matplotlib.pyplot as plt

#x = np.linspace(0, 10, 100)
#y = x**2

#plt.plot(x, y)
#plt.show()

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

Matriz3D = np.array(Matriz3D, dtype = np.int16)
print(Matriz3D)


print(np.zeros((3, 2))) #* Matriz de 0, (3 Renglones,2 Columnas)

print(np.ones((5,7))) #* Matriz de 1, (5 Renglones,7 Columnas)