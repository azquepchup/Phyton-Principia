# Dates

#! Estas son bibliotecas bases, ya dadas, importante, porque no puedo tener otro archivo propio con esos nombres porque entonces ocurren errores.
#datetime  → fechas y horas
#math      → funciones matemáticas
#random    → números aleatorios
#os        → interactuar con el sistema operativo
#json      → leer y escribir JSON


from datetime import datetime as dt #importo de la biblioteca datetime y cambio su nombre a dt

fecha = dt(2024, 2, 11, 4, 5, 1)

now = dt.now() #now es agarra la fecha y hora di mi computadora y la pone aqui

print(now) # lo imprime en la consola

print(now.minute) #dice solo el minuto

from datetime import time

my_time = time(3, 45) #meto una hora la que sea arbitraria

print(my_time.minute) #imprime solo el minuto

from datetime import date # lo mismo, pero con una fecha

my_date = date.today() #imprime la de hoy

print(my_date)

print(my_date.day)

#Operaciones de fechas

new_year = dt(2027, 1, 1)

print(new_year - now)
