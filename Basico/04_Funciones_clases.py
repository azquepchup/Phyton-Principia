# Funciones
sep=123*"="
# ! esto es crítico    | #!
# ? esto es una duda   | #?
# * esto es importante | #*
# todo esto es pendiente | #todo
# // esto está descartado | #//

#* def
#* Literalmente son funciones o hasta mejor aun, como transformaciones lineales *haria falta ver si cumple las propiedades*
def Sum_numbers(numero_1, numero_2): #Dominio R^2 --> R
    print(numero_1 + numero_2) #Regla de correspondencia

#Ejemplo de la función
Sum_numbers(4, 6)
#! Sum_numbers(8) TypeError: Sum_numbers() missing 1 required positional argument: 'numero_2'
#Pero si definimos el numero_2
def Sum_numbers(numero_1, numero_2 = 10): 
    print(numero_1 + numero_2) 

Sum_numbers(8)
#* Pero esto solo sirve si no puse nada, en caso que si:
Sum_numbers(8, 2) #Toma al 2 como prioridad sobre el 10

print(sep)
#* Return
#Retorna el valor que nosotros queramos
def Sum_numbers(numero_1, numero_2):
    print(numero_1 + numero_2)
    return numero_1 + numero_2 #? no entiendo bien como funciona

result = Sum_numbers(5, 6)
print(result)

print(sep)
#* Clases 

class unHumanoRaro:
    def __init__(self, altura, edad, peso): #definimos la funcion
        self.altura = altura #damos "valores a llamar de cada funcion y que nos regresara"
        self.edad = edad 
        self.peso = peso
humano_1 = unHumanoRaro(1.80,23, 87) #Definimos al sujeto que llamara la funcion, lo ponemos dentro de la funcion y le damos valores a cada entrada

print(f"el humano 1 mide {humano_1.altura}m ,pesa {humano_1.peso}kg y tiene edad {humano_1.edad} años") #imprimimos en la consola su estatura, peso y edad

print(sep)
#TODO: Mejorar e implementar como base de mi futuro programa:

class Elementos:
    def __init__(self, nombre, MM, densidad, numero_atomico): #definimos la funcion
        self.Masa_Molar = MM #damos "valores a llamar de cada funcion y que nos regresara"
        self.densidad = densidad 
        self.na = numero_atomico
        self.Elemento = nombre

    def información_elemento(self):
        print(f"{self.Elemento} con numero atomico {self.na}, masa molar {self.Masa_Molar} y densidad {self.densidad} ") #imprimimos en la consola su estatura, peso y edad
    
    def desintegración(self):
        if self.na in Estables:
            print(f"El {self.Elemento} no tiene desintegración beta")
        else: 
            print(f"El {self.Elemento} con numero atomico {self.na} tiene desintegración en desintegración beta")




Bismuto = Elementos("Bismuto", 208.9, 9.8, 83) #Definimos al sujeto que llamara la funcion, lo ponemos dentro de la funcion y le damos valores a cada entrada

Oxigeno = Elementos("Oxigeno", 15.9, 1.42, 8)

Hidrogeno = Elementos("Hidrogeno", 1.007, 0.071, 1)

Boro = Elementos("Boro", 10.811, 2.51, 5)

Estables = [Hidrogeno, Oxigeno]

Bismuto.información_elemento()
Bismuto.desintegración()

Oxigeno.información_elemento()
Oxigeno.desintegración

Hidrogeno.información_elemento()
Hidrogeno.desintegración()

Boro.información_elemento()
Boro.desintegración()