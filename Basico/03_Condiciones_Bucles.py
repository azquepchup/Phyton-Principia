# Condicionales
sep=123*"="
# ! esto es crítico    | #!
# ? esto es una duda   | #?
# * esto es importante | #*
# todo esto es pendiente | #todo
# // esto está descartado | #//



# if, Si pasa esto, entonces x
if 4 < 6:
    print("4 es menor que 6") 

#Si la función no se cumple entonces no se imprime
print(sep)
print
if 4 > 6:
    print("4 es menor que 6") 


numero = 7
if 4 > 6 or numero == 7:
    print(True)

C6H12O7 = "Ácido glucónico"
if len(C6H12O7) > 10:
    print("muy largo")

print(sep)
#else, Si no se cumple el if entonces else

C6H12O7 = "Ácido glucónico"
if len(C6H12O7) > 1000:
    print("muy largo")
else:
    print("no es tan largo")

#Todo en resumen, if si pasa esto, entonces esto, else, si no pasa if entonces pasa esto

print(sep)

#elif, es como una continuación del if, si no se cumple if entonces, pasa a elif que seria como ok no se cumplio lo anterior, pero si se cumple esto, entonces,
if 4 > 6:
    print("4 es menor que 6")
elif numero == 7:
    print("numero es igual a 7")
else:
    print("no se cumplio ninguna condición")

#si no se llega a cumplir ninguna de ambas entonces else.
if 4 > 6:
    print("4 es menor que 6")
elif numero != 7:
    print("numero es igual a 7")
else:
    print("no se cumplio ninguna condición")

print(sep)
# elif podemos tener ninguno o varios
if 4 > 6:
    print("4 es menor que 6")
elif numero != 7:
    print("numero es igual a 7")
elif numero > 1:
    print("mi numero al menos es mayor que 1")
else:
    print("no se cumplio ninguna condición") # este ya no se ejecuta porque elif se cumplio

print(sep)
#Bucles o loops
# Se repita algo hasta que indiquemos que se deje de repetir
numero = 0
#while numero < 10:
  #  print(numero):  #! se ejecuta infinitamente
    
#Para detenerlo

while numero < 20:
    numero += 1
    print(numero)
    if numero < 5:
        print("es menor que 5") 
    elif numero <= 5:
        print("es igual que 5") #* esta accion se pone solo cuando es igual, curiosamente hay como una jerarquia de funciones, como que el if sobre el elif, es decir, no se ponen las dos condiciones o imprime a la vez "es menor que 5" o "es igual que 5"
    elif numero == 13:
        print("es igual a 13")
        break
    elif numero > 5:
        print("es mayor que 5")
        
print(sep)

#for 
lista = [74, 5, 6, 2, 6, 0]
for number in lista:
    print(number)

# puede ser n en vez de number

lista_letras = ["a", "b", "c"]
for character in lista_letras:
    print(character)

#Tambien podemos hacer que imrpima hasta x cosa
for character in range(100+1):
    print(character)

#Es mas facil que sumarle 1 a todo por ejemplo:

for character in range(101):
    print(character)
    if character == 5:
        print("es igual a 5")
        break

print(sep)
print("Fin 1/04/2026, 7:14pm")
print(sep)