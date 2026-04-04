#Zefe de un elemento

#def Zefe(E, n):
#    print(((E * (n**2)) / ((-2.1811e-18)))**(1/2))

#Zefe(-3.94e-18,2) # ! Util, pero no para mi tarea



# Z = número atómico
# mismo_grupo = electrones en el mismo grupo
# grupo_n1 = electrones en grupo n-1
# grupo_n2 = electrones en grupos n-2 o menores

#// Funcional, pero poco eficiente, pienso que podria hacer algo mejor:
#def Zefe(Z, mismo_grupo, grupo_n1, grupo_n2):
#    sigma = (mismo_grupo * 0.35 + grupo_n1 * 0.85 + grupo_n2 * 1)
#    print(round(Z - sigma, 2))
#Zefe(26, 1, 14, 10)


class Elemento:
    def __init__(self, nombre, Z, m_g, g_n1, g_n2):
        self.nombre = nombre
        self.Numero_Atomico = Z
        self.mismo_grupo = m_g
        self.grupo_n1 = g_n1
        self.grupo_n2 = g_n2
        sigma = (self.mismo_grupo * 0.35 + self.grupo_n1 * 0.85 + self.grupo_n2 * 1)
        self.Zef = round(Z - sigma, 2)
        print(f"{self.nombre}: Zef = {self.Zef}")


Mn_Zefe = Elemento("Mn", 25, 1, 13, 10)
Fe_Zefe = Elemento("Fe", 26, 1, 14, 10)
Zn_Zefe = Elemento("Zn", 30, 1, 18, 10)
Cu_Zefe = Elemento("Cu", 29, 0, 18, 10)

if Zn_Zefe.Zef > Cu_Zefe.Zef:
    print(f"{Cu_Zefe.nombre} es más pequeño")
else:
    print(f"{Zn_Zefe.nombre} es más pequeño")