sep=123*"="
# ! esto es crítico    | #!
# ? esto es una duda   | #?
# * esto es importante | #*
# todo esto es pendiente | #todo
# // esto está descartado | #//

#Modulos
#Importar ficheros de otros proyectos para no copiar y pegar codigo, asi ahorrar espacio
#! Para que funcione el nombre de donde importas no tiene que tener numeros y caracteres especiales



#! import Funciones #importa todo el archivo, por lo que ejecuta todo el codigo, pero yo solo quiero una parte entonces:
#! Funciones.Sum_numbers(5, 7)

#from Funciones import Sum_numbers

#! Sum_numbers(3, 7) sigue pasando lo mismo xd, pero bueno lo que pasa es que no es un error, se suele hacer un fichero donde pones funciones sin resultado, asi solo importas las funciones y las ocupas aqui, seria como tener un mega archivo solo de funciones y luego importas todas esas funciones a un nuevo archivo para evitar tener exceso de codigo y ocupas esas funciones en uno nuevo.

#Ejemplo

from Funciones import Suma_Usual

Suma_Usual(1, 4, 5) #Imprime la consola 10

#* PODEMOS CAMBIAR SU NOMBRE 
from Funciones import Producto_Punto as Punto

Punto(1, 2, 3, 5, 6, 7) #Ya no funciona si le ponemos Producto_Punto

print(sep)
print("Final de la primera parte 02/04/2026, 1:05am")
print(sep)