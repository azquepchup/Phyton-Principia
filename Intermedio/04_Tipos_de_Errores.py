#Tipos de errores

#a #NameError: name 'a' is not defined

#print "Hola mundo" #SyntaxError: Missing parentheses in call to 'print'.
#Solucion
print("Hola mundo")

#print(variable) #NameError: name 'variable' is not defined.
#Solucion:
variable = 5
print(variable)

list_variable = [4, 5, 6, 7, 8]
print(list_variable[0])
print(list_variable[1])
print(list_variable[2])
print(list_variable[3])
#print(list_variable[6]) #IndexError: list index out of range

#Solucion: agregar un elemento más a la lista

#import matth #ModuleNotFoundError: No module named 'matth'
#Solucion
import math

#print(math.Pi) #AttributeError: module 'math' has no attribute 'Pi'.
#Solución
print(math.pi)

variable_dict = {"Nombre":"Aranza",
                 "Apodo":"Nicole",
                 "Lengua materna":"Nahuatl"}

#print(variable_dict["Lengua de mamadas"]) #KeyError: 'Apodooo'
#Solución
print(variable_dict["Lengua materna"])