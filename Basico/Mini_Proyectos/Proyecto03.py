
#FIZZBUZZ #3
#Escribe una función que muestre por consola los números 
#de 1 a 100 (ambos incluidos y con un salto de línea entre
#cada impresión), sustituyendo los siguientes:
#- Múltiplos de 3 por la palabra "fizz".
#- Múltiplos de 5 por la palabra "buzz".
#- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 and a % 5 == 0:
            print("fizzbuzz")
        elif a % 3 == 0:
            print("fizz")
        elif a % 5 == 0:
            print("buzz")
        else:
            print(a)

fizzbuzz()