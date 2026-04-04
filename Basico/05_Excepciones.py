#
sep=123*"="
# ! esto es crítico    | #!
# ? esto es una duda   | #?
# * esto es importante | #*
# todo esto es pendiente | #todo
# // esto está descartado | #//

#* Exepciones

#print(1 / 0) ZeroDivisionError: division by zero
#print(5 + "3") TypeError: unsupported operand type(s) for +: 'int' and 'str'

#* try si aplico este codigo no funciona lo llevo al
#* except

try:
    print(5 + "3")
except:
    print("error") #Funciona hasta aqui porque no funciona
else:
    print("funciona")

print(sep)

try:
    print(5 + 3) #! No de ley tiene que ser print, puede solo que haga una acción como es solo sumar 5+3 y si cumple o no, pasar a la siguiente función, en este caso funcionaria por lo que imprime funciona
except:
    print("error")
else:
    print("funciona") #Funciona el codigo e imprime hasta el else, ya que si funciono, entonces no dice "error" y pasa a la siguiente función que seria imprimir "funciona"

print(sep)

try:
    print(5 + "3")
except:
    print("error")
else:
    print("funciona")
finally:
    print("Suma usual") #finally, siempre pasa sin importar que.

# print(cosas) NameError: name 'dadjiadak' is not defined
# podemos hacer que las except solo sean de un error en especifico y si es de otro tipo falla

try:
    print(5 / 0)
except ZeroDivisionError: #si es de otro tipo como un NameError falla el porgrama
    print("error")
else:
    print("funciona")
finally:
    print("Division usual")

print(sep)

try:
    print(5 / 0)
except ZeroDivisionError:
    print("error de tipo ZeroDivisionError")
except NameError:
    print("error de tipo NameError")
else:
    print("funciona")
finally:
    print("Division usual")

print(sep)
#Como ver los errores

try:
    print("hola") #Puse las comillas para que no me siguiera apareciendo error, pero para que funcione tienen que ir sin comillas
except ZeroDivisionError as errorZ:
    print("error de tipo ZeroDivisionError")
except NameError as errorN:
    print("error de tipo NameError")
    print(errorN)
else:
    print("funciona")
finally:
    print("Saludo usual")

print(sep)
print("Final 02/04/2026, 12:34")
print(sep)
