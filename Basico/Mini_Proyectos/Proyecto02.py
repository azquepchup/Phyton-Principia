#CONVERSOR DE TIEMPO #2
#Crea una función que reciba días, horas, minutos y segundos 
#(como 'list') y retorne su resultado en milisegundos.

def Conversion(d, h, m, s):
    return d*8.64e7 + h*3.6e6 + m*6e4 + s*1e3 

resultado = Conversion(0, 0, 0, 0)

print(f"{resultado * 1} ms" )