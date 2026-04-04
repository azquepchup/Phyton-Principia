#Apuntos y formulas de General II


class Expresiones_de_concentracion:
    def __init__(self, g_soluto, g_disolvente, mL_disolución = None, MM = None, densidad_disolución = None):
        self.g_soluto = g_soluto
        self.g_disolvente = g_disolvente
        self.g_disolución = g_disolvente + g_soluto
        self.mL_disolución = mL_disolución
        self.densidad_disolución = densidad_disolución
        self.porciento_masa_masa = round((self.g_soluto / self.g_disolución) * 100, 2)
        self.Masa_Molar = MM
        
        
        if mL_disolución is not None:
            self.mL_disolución = mL_disolución
            self.ppm_v = round((self.g_soluto * 1000) / (mL_disolución / 1000), 2)
            print(f"{self.ppm_v} ppm (mg/L)")
        elif densidad_disolución is not None:
            self.mL_disolución = round(self.g_disolución / densidad_disolución, 2)
            self.ppm_v = round((self.g_soluto * 1000) / (self.mL_disolución / 1000), 2)
            print(f"{self.ppm_v} ppm (mg/L)")
        else:
            print("ppm(v): se necesita volumen o densidad")
        
        if MM is not None:
            self.Mol = round((self.g_soluto / MM), 2)
            if self.mL_disolución is not None:
                self.Molaridad = round((self.Mol / (self.mL_disolución / 1000)), 2)
                print(f"{self.Mol} mol")
                print(f"{self.Molaridad} M")
            else:
                print(f"{self.Mol} mol")
                print("Molaridad: se necesita volumen o densidad")
        else:
            print("Mol y Molaridad: se necesita masa molar")


        self.ppm = round((self.g_soluto / self.g_disolución) * 1e6, 2)
        self.ppb = round((self.g_soluto / self.g_disolución) * 1e9, 2)
        
        print(f"{self.g_disolución}g_disolución")
        print(f"{self.porciento_masa_masa}%m/m")
        print(f"{self.ppm}ppm (mg/kg)")
        print(f"{self.ppb}ppb")
        print(f"{self.mL_disolución}mL_disolución")
        print(f"{self.Mol}mol")


#g_soluto, g_disolvente, mL_disolución = None, MM = None, densidad_disolución = None
cosa = Expresiones_de_concentracion(25, 30, None, 58.44, None)
