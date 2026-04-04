#Sets
print("Inicio 30/03/2026")
sep=123*"="
# ! esto es crítico    | #!
# ? esto es una duda   | #?
# * esto es importante | #*
# todo esto es pendiente | #todo
# // esto está descartado | #//
print(sep)
my_set = {} 
print(type(my_set)) #si esta vacio es un "dict"

my_set_lenguaje = {"Python", "JavaScript", "C++"}

print(my_set_lenguaje)
print(type(my_set_lenguaje)) #si tiene elementos es un "set"
#! Puedo notar que no tiene orden los elementos de un set, cada vez que ejecuto el codigo el orden cambia
#? Esto para que me sirve?
#print(my_set_lenguaje[0]) #! TypeError: "set" object is not suscriptable, No tiene sentido preguntarle 

my_set_lenguaje.add("C++")
print(my_set_lenguaje) #No se pueden repetir elementos

my_set_lenguaje.add("C#")
print(my_set_lenguaje) 

print(sep)
#=============================================================================================================
my_newset = {"agua", "fuego", "gaseoso", "cojon de gabo izquierdo"}
print(my_newset)
print(type(my_newset))

my_newset.difference_update(my_set_lenguaje) #dice elementos diferentes de un set a otro
print(my_newset)
print(sep)
#Uno más notorio
my_set_lenguaje = {"Python", "JavaScript", "C++"}
my_set_lenguaje2 = {"Python", "JavaScript", "C++", "C#", "Scrach", "C"}
print(my_set_lenguaje)
print(my_set_lenguaje2)
my_set_lenguaje2.difference_update(my_set_lenguaje)
print(my_set_lenguaje2) #Me dice las diferencias del 2 con respecto al 1,es como la resta de conjuntos en matemáticas

#? Que pasaria si lo hago al reves?
#! Me di cuenta que tengo que volver a definirlos, porque si no ocurre que estoy comprando con el anterior "nuevo" my_set_lenguaje y no el original
my_set_lenguaje = {"Python", "JavaScript", "C++"} 
my_set_lenguaje2 = {"Python", "JavaScript", "C++", "C#", "Scrach", "C"}
print(my_set_lenguaje)
print(my_set_lenguaje2)
my_set_lenguaje.difference_update(my_set_lenguaje2)
print(my_set_lenguaje) #Me dice las diferencias del 1 con respecto al 2,es como la resta en matemáticas, en este caso pone set()
#? Por qué sucede esto?
#Tomando como analigia lo de la resta en matematicas, no es lo mismo A\B que B\A, por lo que en el primer caso seria como B\A que me es la resta de los elementos iguales en B y A y el resultado son los elementos que quedan en B, ahora bien, para el otro seria como A/B como los elementos B tiene los mismos elementos de A y un par más la resta seria el vacio.

print(sep)
#=============================================================================================================
#* Ejemplo practico dado por Claude en respuesta a mi duda en la linea 13

experimento_1 = {"H", "O", "Na", "Cl", "Fe"}
experimento_2 = {"H", "O", "Ca", "Mg", "Fe"}

# ¿Cuáles aparecen en ambos?
print(experimento_1 & experimento_2)

# ¿Cuáles son exclusivos del experimento 1?
print(experimento_1 - experimento_2)

# ¿Cuáles aparecen en cualquiera de los dos?
print(experimento_1 | experimento_2)
#&  →  A ∩ B  (intersección)
#-  →  A \ B  (diferencia)
#|  →  A ∪ B  (unión)
print(sep)
#=============================================================================================================

#Diccionarios

my_dict = {"a", "b"}
print(my_dict)
print(type(my_dict)) #dice set, pero es porque no esta bien hecha el diccionario:

print(sep)
#=============================================================================================================
my_dict = {"Nombre":"Aranza", "Apellido":"papu", "Apodo":"Ari"}
print(my_dict)
print(type(my_dict))
#* Para que no quede tan largo puedo hacer enter:
my_dict = {"Nombre":"Aranza",  
            "Apellido":"papu", 
            "Apodo":"Ari"}
print(my_dict)
print(type(my_dict))

print(my_dict["Apodo"])
#? Puedo saber especificamente que tipo de elemento es cada cosa en un dict? Pienso que si, formulo una forma
print(type(my_dict["Apodo"])) #* Se puede de esta forma!

print(my_dict["Nombre"])
print(my_dict["Apellido"])
print(my_dict["Apodo"])

#* Lo importante es que a diferencia de las listas, los diccionarios no solo pueden ser guardadas deacuerdo a la posición, si no que tambien se pueden guardar con str, Int, Floot, etc.
my_newdict = {5:"Cinto",
            10:"Diez",
            "Veinte":20,
            "pi":3.1415,
            2.718281:"e",
            "Mayor que":5>3}
print(my_newdict)

print(my_newdict.keys()) #imprime las llaves, es decir, la primera parte de la definición de las llaves, lo podria hacer como un simil con una función, como su dominio, su contradominio seria el despues de los 2 puntos, es un simil raro, creo que podria encontrar algo mejor
#? Con lo anterior dicho me surgio una duda para mejor simil, una forma que lo pense fue como conjuntos, pero no se si los dict pueden contener otras listas o un set, porque ya vi que pueden ser las entradas y las salidas cualquier cosa comun, como un str, Int, Floot, Booliano
prueba = {4:"Cuatro",
            "Nuevo_set":{"caca", "pipi", "popo", "miados",5,2,3,1},
            "Nueva_lista":[123,"sis","nos", True, 3.1415]
            }
print(prueba) #!Funciona
print(prueba.keys()) #El valor de la pre-imagen
print(prueba.values()) #Valor de la imagen
print(prueba[4])
print(prueba["Nuevo_set"])
print(prueba["Nueva_lista"])
# Concluyo que si podria definirlo más parecido como conjuntos, como conjuntos dentro de conjuntos.
#Todo, Esta pregunta queda pendiente
#? Ahora pienso en que podria hacer ver cada elemento de de su imagen o como dije de su contradominio de cada elemento del diccionario, pero la verdad no se me ocurre como hacerlo
#Todo

print(sep)
#* Puedo cambiar mi lista a diccionario 
prueba = list(prueba)
print(prueba) # Pone los valores de la pre-imagen (Forma correcta de llamarle son llaves)
my_dict = set(my_dict)
print(my_dict)
my_newdict = tuple(my_newdict)
print(my_newdict)
#Todo
#? Se pierde información al volverlo una lista, tupla o set, es decir, solo se ven las llaves, cuando imprimo el codigo ya cambiado a una list, etc, que le pasan a las imagenes (no sé como se llaman)?
#Todo pendiente para mañana es resolver esta ultima duda y las que me quedaran en el camino.
print("Fin por hoy, 31/03/2026 a las 1:13am")
