# Funciones de Orden Superior

def add_value(num):
    return num + 5

def add_value_2(num):
    return num + 10

def sum_values(num1, num2, f):
    return f(num1 + num2)

print(sum_values(3, 7, add_value)) #lo hago en funcuon de la primera
print(sum_values(3, 7, add_value_2)) #lo hago en funcion de la segunda

#Closures

def closure_number():
    def closure_new(num):
        return num + 5
    return closure_new

my_fun = closure_number()
print(my_fun(2))

def closure_number(original_number): #numero fijo en este caso al final sera un 3 con el valor dado
    def closure_new(num): #numero igual arbitrario al final dado
        return num + 5 + original_number # la funcion que se ejecuta
    return closure_new 

my_fun = closure_number(3) #numero arbitrario de la primera función
print(my_fun(2)) #numero arbitrario de la segunda función

#map
list_numbers = [1, 5, 11, 52]

def division_number(number):
    return number / 2

request = list(map(division_number, list_numbers))
print(request)


#* Tambien se puede hacer con lambdas

def division(numb):
    return numb / 2

req = list(map(lambda numb: numb * 2, list_numbers))

print(req)

#filter

def filter_number(number):
    return number > 10

request = list(filter(filter_number, list_numbers)) #filtra hasta 10 por la función
request = list(filter(lambda number: number > 15, list_numbers)) #filtra hasta 15

print(request)