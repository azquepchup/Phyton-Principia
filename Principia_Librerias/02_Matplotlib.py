#Matplotlib 
import matplotlib
matplotlib.use('TkAgg')   # Fuerza el backend interactivo

sep = "=" * 120
# %% [celda 1 - imports]
import numpy as np
import matplotlib.pyplot as plt
#%%


import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt


x = [2023, 2024, 2025, 2026]
y = [15, 27, 39, 86]

plt.plot(x, y) #Grafica x, y

plt.show() #Mostrar la grafica

#solo para un eje
plt.plot(x)
plt.show()

#Como habiamos visto en Numpy las listas son más rapidas
import numpy as np

x = np.array([2, 4, 6, 8, 10])
y = np.array([3, 1 , 6, 47, 49])

plt.plot(x, y)

plt.show()

#Pineso en hacer una función que como en matematicas, entren numeros saquen otros #? Para hacerlo formal tendria que dar contradominio, dominio y regla de correspondencia, el problema es que si el numero de elementos de una lista son diferentes que otra no se puede graficar

x = np.linspace(0, 100, 500)

def exponencial(x):
    return 2.71828181**x
y_exp = exponencial(x)

plt.plot(x, y_exp)

plt.show() #arreglar esto, no da lo que espero #? como generaba listas de numeros hasta x

#* Tambien podria hacerlo con la función exponencial ya dada por numpy
#np.exp(x)

#Marcadores

x = np.linspace(0, 5, 20)

def exponencial(x):
    return 2.71828181**x
y_exp = exponencial(x)

y2 = np.random.random(20) * 100



plt.plot(x, y_exp, marker = ".", #marca cada punto con un puntito, puede ser varias, y hay listas de cuales.
                    markersize = 10,#Hace 10 veces más grandes lo marcadores o se puede abreviar como #! "ms" 
                    markerfacecolor = "#B19CD9", #pueden el nombre del color, valores rgb, valores hexadecimales o valores cmyk
                    markeredgecolor = "#1cd3fc", # Color del borde #! abreviado med
                    linestyle = "dashed", #Estilo de linea #None ninguna linea, solo los puntos
                    linewidth = 2, #Ancho de linea
                    color = "red") #Color de la linea

plt.plot(x, y2)

plt.show()

print(sep)
# =====================================
#! Descubri como ver la grafica directamente sin tener que ejecutar todo el codigo, solo una parte, se pone "#%%" y luego se da shift + Enter  y se ejecuta
#! Primero se debe ejecutar la celda donde importo todo, porque es un entorno virtual por lo que entiendo es donde se ejecuta una parte de mi codigo en especifico, creo que no debe de ser necesariamente una grafica, puede ser lo que sea, pero es especialmente util en graficas, para no ejercutar todo el codigo y que aparezcan todas las graficas 1 por 1, ademas es más rapido de solucionar codigo localizado, fuera de eso su funcionamiento por lo que entiendo es asi, es un entorno vitual, como una maquina vitual y el kernel es el la maquina que lo ejecuta
#! Si se traba borrar todo darle a restart para que vuelva a iniciar
#! Se tiene que importar en un "#%%" las bibliotecas que vaya a ocupar para que en futuros "#%% se ejecute":
# %% [celda 1 - imports]
import numpy as np
import matplotlib.pyplot as plt

#%%

#Titulos a las graficas
plt.title("Class size",fontsize = 25, #Tamaño
                        family = "Adwaita Sans", #Tipo de letra
                        fontweight = "bold", #Negritas
                        color = "#000000", #Color del titulo
                        )

#Titulo para el eje x
plt.xlabel("Reales radoms del 0.1 al 5", fontsize = 10, #Tamaño
                                        family = "Adwaita Sans", #Tipo de letra
                                        fontweight = "bold", #Negritas
                                        color = "#800080" #Color del titulo
                                        )
#Titulo para el eje y
plt.ylabel("Reales", fontsize = 10, #Tamaño
                    family = "Adwaita Sans", #Tipo de letra
                    fontweight = "bold", #Negritas
                    color = "#800080" #Color del titulo
                    )

x = np.linspace(0.1, 5, 100)

y_exp = np.exp(x)
y_log = np.log10(x)

line_style = dict(  marker = ".", #Para no siempre poner un mega codigo, podemos comprimirlo en un diccionario y luego descromprimirlo en el plot
                    markersize = 7,
                    markerfacecolor = "#000000", 
                    markeredgecolor = "#FFFFFF", 
                    linestyle = "solid",
                    linewidth = 4
                    )


y_3 = np.linspace(0.1, 5, 100)

#label = nombre de la grafica
#Para que se pongo los nombres debo ejecutar plt.legend()

plt.plot(x, y_exp, **line_style, color = "green", label ="exp(x)") #Descomprimimos aqui con ** 

plt.plot(x, y_log, **line_style, color = "red", label ="log10(x)") #Podemos cotar una cosa especifica del dict de la linea y ponerla como un argumento en especifico.

plt.plot(x, y_3, **line_style, color = "blue", label ="lineal") #Asi mantengo todo el estilo de linea, pero modifico especificamente el color de la linea

#plt.xticks(x) #Forzar para que las marcas sean para cada valor de x, pero seria un caos por todos los valores que hay lo mejor #? paro para este caso como seria mejor, para poner uno cada 0.2 o asi?
#cambiar parametros para ambos, en este caso pintar los titlos para ambos
plt.tick_params(axis = "both", #podemos seleccionar x o y o ambos
                colors = "#00FF00" #Colores en plural
                )

#lIneas de cuadricula
plt.grid(axis = "both",
        linewidth = 2,
        color = "lightgray",
        linestyle = "dashed"
        )  
#Si ponemos dentro axis = "x, y o ambos" 


plt.legend()
plt.show()

# ===================================
#%% 
#Grafico de barras

categorias_de_comida = np.array(["Frutas", "Verduras", "Dulces", "Enchiladas", "Carne"])
Gente_a_la_que_les_gusta = np.array([4, 1, 10, 7, 2])

plt.bar(categorias_de_comida, Gente_a_la_que_les_gusta)

plt.title("Consumo de comidas")

plt.xlabel("Tipo de Comida")
plt.ylabel("Numero de gente que la consume")
#* Se puede aplicar como en el anterior varias acciones a la grafica, colores, tipo de letra, tamaño, etc

plt.bar(categorias_de_comida, Gente_a_la_que_les_gusta, color = "pink")
#plt.barh hace el grafico de barras horizontales

plt.show()

#======================================================================
# %%
#Grafico circular

Semestre = np.array(["1er", "2do", "3er", "4to", "5to", "6to", "7mo"])
Estudiantes = np.array([20, 124, 35, 75, 45, 13, 2])

Colores = ["red", "blue", "yellow", "green", "purple", "lightgray", "orange"]

plt.pie(Estudiantes, labels = Semestre, #Mostrar los nombres
                    autopct = "%1.1f%%", #Porcentaje ponemos el que sea con 1.1 decimal y que tenga signo % y que la haga en % por eso 2 %
                    colors = Colores, #Colores
                    explode = [0, 0.1, 0, 0, 0, 0, 0.5], #Separa partes de la grafica, asi resalta más
                    shadow = True, #Activar una sombra
                    startangle = 30 #Girar la grafica
                    )

plt.title("Gente en el semestre")


plt.show()

#====================================================
# %%
#Grafico de dispersión

#Estudiar n horas vs Nota en un examen 

x1 = np.array([0, 1, 2, 2, 3, 4, 4, 5, 7, 9]) #Horas de estudio grupo 1 
y1 = np.array([55, 60, 61, 65, 70, 72, 75, 80, 83, 90]) #Nota del examen grupo 1

x2 = np.array([0, 1, 2, 3, 3, 4, 6, 8, 10, 12]) #Horas de estudio grupo 2
y2 = np.array([49, 50, 61, 70, 72, 80, 85, 90, 97, 100]) #Nota del examen grupo 2

Estilo_puntos = dict(alpha = 0.7,#Transpariencia (Rango de 0 a 1)
                s = 20)#Tamaño de los puntos

plt.scatter(x1, y1, **Estilo_puntos,
                    color = "blue",
                    label = "Grupo 1")

plt.scatter(x2, y2, **Estilo_puntos,
                    color = "red",
                    label = "Grupo 2")



from scipy import stats
# --- 1. Calcular la línea de tendencia (mínimos cuadrados) ---
# linregress te da: pendiente, intercepto, r-value, p-value, error estándar
# slope (pendiente), intercept (intersección), r_value (coeficiente de correlación de Pearson), p_value (valor p),std_err (error estándar de la pendiente), std_err (error estándar de la pendiente)
slope, intercept, r_value, p_value, std_err = stats.linregress(x1, y1)
print(f"La ecuación de la recta es: nota = {slope:.2f} * horas + {intercept:.2f}")
print(f"Coeficiente de correlación (R): {r_value:.3f}")

# --- 2. Crear los puntos de la recta para graficar ---
# Generamos una línea suave usando muchos puntos entre el mínimo y máximo de 'horas'
x_tendencia = np.linspace(min(x1), max(x1), 100)
y_tendencia = slope * x_tendencia + intercept

# --- 3. Visualización ---
plt.figure(figsize=(8, 5))
plt.scatter(x1, y1, color='purple', label='Datos reales')
plt.plot(x_tendencia, y_tendencia, color='green', linestyle='--', label='Línea de tendencia')




plt.title("Resultados de examenes")
plt.xlabel("Horas estudiadas")
plt.ylabel("Nota del examen")
plt.legend()
plt.grid(True, 
            linestyle='--', 
            alpha=0.3)

print(sep)
print("RESULTADOS DE REGRESIÓN LINEAL")
print("="*30)
print(f"Pendiente (slope):     {slope:.4f}")
print(f"Intercepto:            {intercept:.2f}")
print(f"Coef. correlación (R): {r_value:.4f}")
print(f"R² (coef. determinación): {r_value**2:.4f}")
print(f"Valor p:               {p_value:.4e}")
print(f"Error estándar slope:  {std_err:.4f}")
print(sep)


plt.show()





