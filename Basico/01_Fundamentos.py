#Hola como estas? #comentario
print("Hola mundo")

#Tipos de datos
print(type("Hola mundo")) #String

#texto
print(type("hola mundo"))
print(str) 

#Numero
print(type(42)) #Int
print(type(3.14)) #Float

#Variables
a=4
print(a)
b=3.14
print(b)
c=a+b
print(c)

Mi_texto="Hola mundo"
print(Mi_texto)

Caca= "Esto es una variable con un nombre poco apropiado"
print(Caca)
print(type(Caca))

Mi_numero_favorito=3.14
print(Mi_numero_favorito)
print(type(Mi_numero_favorito))

#Concatenacion
print(Mi_numero_favorito, Caca)

print("mi numero favorito es:", Mi_numero_favorito)
print("Mi numero favorito es:", Caca)
#====================================================================================================
#Operadores aritmeticos
print(6+4) #suma usual
print(6-4) #resta usual
print(6*4) #multiplicacion usual
print(6/4) #division usual
print(6%4) #division entera, devuelve el resto de la division
print(3%2) #division entera, devuelve el resto de la division
print(3**3) #potencia
print(3*3*3) #multiplicacion de 3 por si mismo 3 veces, es lo mismo que 3**3
print(11//3) #division entera, devuelve en el entero resultante de la division "floor division"
print(11/3) #division usual, devuelve con el numero decimal 

print("hola"+" mundo") #suma de strings, se llama concatenacion
print("hola"*3) #repite el string 3 veces
print(Caca*3) #repite el string 3 veces
print(Mi_texto*3) #repite el string 3 veces
print("Hola"+ str(3)) #concatenacion de string con numero, se convierte el numero a string con str() para poder concatenar
print("Hola"+str(Mi_numero_favorito)) #concatenacion de string con numero, se convierte el numero a string con str() para poder concatenar
print("Hola"+"3")
print(a)
#print("Hola "+a) #esto da error porque no se puede concatenar un string con un numero, hay que convertir el numero a string con str()
print("Hola + " + str(a))


#Operadores comparativos

#Booleanos
#Los operadores comparativos devuelven un valor booleano, es decir, True o False
#Int & Float
print(6>4) #mayor que
print(6<4) #menor que
print(6>=4) #mayor o igual que
print(6<=4) #menor o igual que
print(6==4) #igual que 
print(6!=4) #diferente que

#Strings
print("hola">"mundo")
print("hola"=="bola")
print("hola">"bolas") 
print(len("hola")>len("bolas")) #compara numero de letras de cada string
print("b">"a") #entonces lo que cuenta es el orden alfabetico, "b" esta despues de "a" en el alfabeto, por lo tanto "b" es mayor que "a"
print("aaa"<"aba") #a=a y pasa a la siguiente letra a<b, entonces "aaa" es menor que "aba"

#Operadores logicos

#and & or
print(4<6 and 7>9) #and devuelve True si ambas condiciones son True, en este caso devuelve False porque 7>9 es False
#print("True" and "False")=False

print(4<6 or 7>9) #or devuelve True si al menos una de las condiciones es True, en este caso devuelve True porque 4<6 es True
#print("True" or "False")=True porque al menos 1 es true,(logica)

#not
print(not(4<6))#not devuelve el valor contrario, en este caso devuelve False porque 4<6 es True
#print(not("True"))=False porque 4<6 es True, entonces not 4<6 es False

#Ejercicio: print((not(7!=7) and 6>5) and ("rozar"<"rotar" or not (3==5)))
#(notfalse and true) and (false or not false)
#(true and true) and (false or true)
#true and true and true
#true
#Comprobacion:
print((not(7!=7) and 6>5) and ("rozar"<"rotar" or not (3==5)))

#Comentarios            Comando de activasión de comentarios
# ! esto es crítico    | #!
# ? esto es una duda   | #?
# * esto es importante | #*
# todo esto es pendiente | #todo
# // esto está descartado | #//
# # esto es un comentario normal | #

separador = "="
print(separador) #imprime el separador



print("Final, esto es el final de hoy 29/03/2026")
print("=" * 123) #imprime el separador 123 veces, es decir, una linea de 123 guiones
# =====================================================================================================

#Segunda parte 30/03/2026

#Strings
#* Se pueden escribir Strings con comillas simples ' ' o con comillas dobles " "
print("Hola mundo") #String con comillas dobles
print('Hola mundo') #String con comillas simples

#Aun si son diferentes, ambos son Strings, es decir, ambos son del tipo str y se pueden concatenar entre si
print("Hola" + ' mundo') #concatenacion de string con comillas dobles y string con comillas simples, se puede concatenar porque ambos son del tipo str
print("Hola" + ' ' + "mundo" ) #Tambien se pueden concatenar Str multiples veces y combinar las comillas simples y dobles, se puede concatenar porque ambos son del tipo str

#! Esto es muy pesado para el sistema
print("esto es un texto de una variable" + Mi_texto + "y esto es otro texto de otra variable" + Caca) #concatenacion de string con variables, se puede concatenar porque ambos son del tipo str

#! Entonces se pone:
print(f"esto es un texto de una variable {Mi_texto} cacacaca") #concatenacion de string con variables, se puede concatenar porque ambos son del tipo str, se usa f antes de las comillas para indicar que se va a usar formato de string, y se usan llaves {} para indicar donde se va a insertar la variable

other_string="Hola"
h,i,j,k = other_string #desempaquetado de string, se asigna cada letra del string a una variable diferente, en este caso h='H', i='o', j='l', k='a'
print(h) 
print(i)
print(j)
print(k)
print(f"{h}{i}{j}{k}") #concatencacion de las variables h, i, j, k para formar el string "Hola"
print(other_string)

print(separador*123)
# =====================================================================================================
#! Funciones mas comunes en strings
other_string="Hola"
print(other_string.upper()) #convierte el string a mayusculas
print(other_string.lower()) #convierte el string a minusculas
print(other_string.capitalize()) #convierte la primera letra a mayuscula
print(other_string.title()) #convierte la primera letra de cada palabra a mayuscula
print(other_string.swapcase()) #convierte las mayusculas a minusculas y viceversa
print(other_string.strip()) #elimina los espacios en blanco al principio y al final
print(other_string.lstrip()) #elimina los espacios en blanco al principio
print(other_string.rstrip()) #elimina los espacios en blanco al final
print(len(other_string)) #Cuenta el numero de caracteres del sting, incluyendo los espacios en blanco
print(other_string.count("o")) #Cuenta el numero de veces que aparece la letra "o" en el string
print(other_string.find("o")) #devuelve la posicion de la primera aparicion de la letra "o" en el string, si no se encuentra devuelve -1



Mi_texto="Hola mundo"
print(Mi_texto.upper())
print(Mi_texto.lower())
print(Mi_texto.capitalize())
print(Mi_texto.title())
print(Mi_texto.swapcase())
print(Mi_texto.strip())
print(Mi_texto.lstrip())
print(Mi_texto.rstrip())
print(len(Mi_texto))
print(Mi_texto.count("o"))
print(Mi_texto.find("o"))

#Varias funciones al mismo tiempo
print(Mi_texto.lower().count("o")) #convierte el string a minusculas y luego cuenta el numero de veces que aparece la letra "o" en el string, en este caso devuelve 2 porque hay 2 letras "o" en el string "Hola mundo")
print(Mi_texto.upper().isupper()) #convierte el string a mayusculas y luego pregunta si el string esta en matusculas



print(separador.count("=")*123)

#=======================================================================================================
#? Tengo una nueva idea para un separador
#En vez de hacer que se multiplique el la variable separador*123
#Puedo hacer una variable que se llame sep y sea 123=

sep=123*"="

print(sep)
#y de esta puedo ahora sin que suene redundante contar sus elementos si llego a olvidarme de cuantos son
print(len(sep))
#or
print(sep.count("="))


print(sep)
#=======================================================================================================

#Listas
    #nuevo tipo de variable

my_list_lenguajes=["Python", "Java", "C++"]
print(my_list_lenguajes) #imprime la lista completa
print(type(my_list_lenguajes)) #imprime el tipo de la variable en este caso es un list
print(my_list_lenguajes[0]) #imprime el primer elemento de la lista, en este caso "Python"
print(my_list_lenguajes[1]) #imprime el segundo elemento de la lista, en este caso    "Java"
print(my_list_lenguajes[2]) #imprime el tercer elemento de la lista, en este caso "C++"

# todo esto es pendiente y lo sigo en 231
#Lista con varios tipos de datos: string, int, float, list, boolean
my_newlist=[123, 3.14, "Hola mundo", [1,2,3], True] #* puedo poner varios tipos de datos en una lista, incluso otra lista dentro de la lista
print(my_newlist) #imprime la lista completa

#Pense en que podria decir el tipo de elemento de cada lista de su posición
print(type(my_newlist)) #imprime el tipo de la variable en este caso es un list
print(type(my_newlist[0])) #imprime el tipo del primer elemento de la lista, en este caso es un int
print(type(my_newlist[1])) #imprime el tipo del segundo elemento de la lista, en este caso es un float
print(type(my_newlist[2])) #imprime el tipo del tercer elemento de la lista, en este caso es un string
print(type(my_newlist[3])) #imprime el tipo del cuarto elemento de la lista, en este caso es un list
print(type(my_newlist[4])) #imprime el tipo del quinto elemento de la lista, en este caso es un boolean

#Ahora pense en que podria hacer una lista que tenga el tipo de cada elemento en la misma posición que el elemento de la lista original
my_newlist_types=[type(my_newlist[0]),type(my_newlist[1]),type(my_newlist[2]),type(my_newlist[3]),type(my_newlist[4])] #* creo una nueva lista que contiene el tipo de cada elemento de la lista original en la misma posición
print(my_newlist_types) #imprime la lista de tipos de cada elemento de la lista original en forma de lista, asi tendria los tipos de elementos que son en forma de lista y no una cada uno y asi evito llenar la terminal

print(sep)
#=====================================================================================================
# todo esto es pendiente, contuniacion de la linea 214

#Lista con varios tipos de datos: string, int, float, list, boolean
my_newlist=[123, 3.14, "Hola mundo", [1,2,3], True] #* puedo poner varios tipos de datos en una lista, incluso otra lista dentro de la lista
print(my_newlist) #imprime la lista completa

print(my_newlist[1]) #me da el segundo elemento para el primer elemento debo comenzar desde el 0
print(my_newlist[0]) #me da el primer elemento de la lista
#print(my_newlist[5]) #esto da error porque no hay un elemento en la posicion 5, la lista tiene 5 elementos pero el ultimo elemento esta en la posicion 4 porque se comienza a contar desde el 0

#Tambien se puede llamar las variables dentro de la lista con negativos:
print(my_newlist[-1]) #me da el ultimo elemento de la lista, en este caso True
print(my_newlist[-2]) #me da el penultimo elemento de la lista, en este caso [1,2,3]
print(my_newlist[-3]) #me da el antepenultimo elemento de la lista, en este caso "Hola mundo"
print(my_newlist[-4]) #me da el anteantepenultimo elemento de la lista, en este caso 3.14 
print(my_newlist[-5]) #me da el primer elemento de la lista, en este caso 123
#y asi si tuviera una lista mas grande, entonces podria seguir llamando los elementos de la lista con negativos hasta llegar al primer elemento que seria my_newlist[-5]
#print(my_newlist[-6]) #esto da error porque no hay un elemento en la posicion -6, la lista tiene 5 elementos pero el primer elemento esta en la posicion -5 porque se comienza a contar desde el -1 hacia atras

#Funciones a las listas
my_newlist.append("Nuevo elemento") #* agrega un nuevo elemento al final de la lista, en este caso "Nuevo elemento"
print(my_newlist)
my_newlist.insert(2,"Nuevo elemento en la posicion 2") #* agrega un nuevo elemento en la posicion 2 de la lista, en este caso "Nuevo elemento en la posicion 2"
print(my_newlist)
my_newlist.remove(3.14) #* elimina el elemento 3.14 de la lista, en este caso el segundo elemento de la lista
print(my_newlist)
my_newlist.pop(5) #* elimina el elemento en la posicion 5 de la lista, en este caso el ultimo elemento de la lista que es "Nuevo elemento"
#print(my_newlist.pop(5)) #* elimina el elemento en la posicion 5 de la lista y lo devuelve, en este caso el ultimo elemento de la lista que es "Nuevo elemento", pero como ya se elimino en la linea anterior, entonces da error porque no hay un elemento en la posicion 5
print(my_newlist)
print(my_newlist.pop(2)) #* elimina el elemento en la posicion 2 de la lista y lo devuelve, en este caso "Nuevo elemento en la posicion 2"
print(my_newlist)

my_newlist.append([1,1,1,5,2,4,3]) #* agrega varios elementos al final de la lista, en este caso 1,1,1,5,2,4,3
print(my_newlist)

# TODO duda pendiente: ¿Cómo puedo agregar varios elementos a la lista de una vez sin que se agregue una lista dentro de la lista?
#? mi objetivo era agregar de una varios numeros para luego ocupar la funcion .count, queria agregar varios de una vez, pero me marca error, que funcion hace que agrege varios elementos a la lista de una vez? Claro porque lo que agregue no fueron varios elementos, fue un solo elemento que es una lista, entonces lo que se agrego fue una lista dentro de la lista, entonces para agregar varios elementos de una vez a la lista, se puede usar la funcion .extend() que agrega cada elemento de la lista que se le pasa como argumento a la lista original, entonces si quiero agregar los numeros 1,1,1,5,2,4,3 a la lista original, entonces que funcion debo agregar, para que no sea uno por uno?
my_newlist.extend([1,1,1,5,2,4,3]) #* agrega varios elementos a la lista de una vez, en este caso 1,1,1,5,2,4,3
print(my_newlist)
print(my_newlist[-1])

#ahora quiero saber cuantas veces se repite el numero 1 en la lista, entonces uso la funcion .count() que cuenta el numero de veces que aparece un elemento en la lista
print(my_newlist.count(1))

#! los elementos deben ser del mismo tipo ejemplo agregare un 1, pero sera  str: "1" entonces no se contara como un 1, sino como un string "1"
my_newlist.append("1") #agrega el string "1" a la lista
print(my_newlist)
#ahora quiero contar los unos, teoricamente tendria que ser la misma cantidad que antes, es decir 4
print(my_newlist.count(1)) 
#efectivamente es 4 y no 5, porque el ultimo elemento "1" es un string y no un int.

#reverse (escribe la lista al reves)
my_newlist.reverse()
print(my_newlist)

#y si quiero limpiar la lista, es decir eliminar todos los elementos de la lista, entonces uso la funcion .clear() que elimina todos los elementos de la lista, dejando una lista vacia
my_newlist.clear()
print(my_newlist) #imprime la lista vacia []

print(sep)
#=====================================================================================================
#Tuplas
my_tupla=(53, 3, "Hola mundo", [1,2,3], True) #* las tuplas son similares a las listas pero no se pueden modificar, es decir, no se pueden agregar ni eliminar elementos de la tupla, pero si se pueden acceder a los elementos de la tupla con su indice
print(my_tupla) 
print(type(my_tupla)) #imprime el tipo de la variable en este caso es un tuple
print(my_tupla[1]) #imprime el segundo elemento de la tupla, en este caso 3
print(my_tupla.count(53)) #cuenta el numero de veces que aparece el elemento 53 en la tupla, en este caso devuelve 1 porque el elemento 53 aparece una sola vez en la tupla
print(my_tupla.index(True)) #devuelve la posicion del primer elemento True en la tupla, en este caso devuelve 4 porque el elemento True esta en la posicion 4 de la tupla

#! NO se pueden modificar las tuplas, entonces no se pueden agregar ni eliminar elementos de la tupla, pero si se pueden acceder a los elementos de la tupla con su indice
#!my_tupla.append("Nuevo elemento") #esto da error porque no se pueden modificar las tuplas, no se pueden agregar elementos a la tupla
#!my_tupla.remove(3) #esto da error porque no se pueden modificar las tuplas, no se pueden eliminar elementos de la tupla
#!my_tupla.pop(1) #esto da error porque no se pueden modificar las tuplas, no se pueden eliminar elementos de la tupla

#* Algo importante que tiene python es que es de tipado debil, es decir, que una variable puede cambiar de tipo, entonces si quiero modificar la tupla, lo que puedo hacer es convertir la tupla a una lista, modificar la lista y luego convertir la lista a una tupla nuevamente, entonces podria hacer algo como esto:
my_tupla=list(my_tupla) #* convierto la tupla a una lista para poder modificarla
print(type(my_tupla)) #imprime el tipo de la variable en este caso es un list
print(my_tupla) #imprime la lista convertida de la tupla
my_tupla.pop() #* elimino el ultimo elemento de la lista, en este caso el elemento True
print(my_tupla) #imprime la lista sin el ultimo elemento

my_tupla=tuple(my_tupla) #* convierto la lista a una tupla nuevamente para que vuelva a ser una tupla
print(type(my_tupla)) #imprime el tipo de la variable en este caso es un tuple
#Fin por hoy 30/03/2026
print("fin del codigo, 30/03/2026")
print(sep)
#====================================================================================================