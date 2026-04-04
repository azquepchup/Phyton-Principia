#EL SEGUNDO MAS GRANDE #1
#En una 'lista' de números, retorna el segundo número más grande.
#Ejemplo: [5,7,2,7,9,4,8]

Numeros = [5,7,2,7,9,4,8]
Copia = Numeros.copy()

Copia.remove(max(Copia)) #remuevo el numero mas grande de la copia
print(max(Copia))   # segundo más grande
print(Numeros)      # lista original intacta
