# Lambdas

my_lambda = lambda num1, num2: num1 +num2 #Funciones, pero como más simples
print((my_lambda(5, 4))) #mas optimas

#* Lambdas funcinan dentro de funciones:
def def_lambdas(value):
    return lambda number: 2 * value + number

print(def_lambdas(5)(5))