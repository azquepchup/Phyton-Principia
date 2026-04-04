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


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = x**2

plt.plot(x, y)
plt.show()