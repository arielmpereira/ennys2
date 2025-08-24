import json
from herramientas.lector import Lector
from herramientas.fechas import edad, edad_meses
from herramientas.subsets import TablaConVariable

class Tablas:
    def __init__(self, archivo_encuesta, archivo_alimentos, archivo_configuracion):
        self.archivo_encuesta = archivo_encuesta
        self.archivo_alimentos = archivo_alimentos
        with open(archivo_configuracion, "rt") as f:
            self.configuracion = json.load(f)
    
    def tabla_encuesta(self):
        l = Lector(self.archivo_encuesta)
        df = l.extracto_variables(self.configuracion["encuesta"]["variables"], variables_fecha=self.configuracion["encuesta"]["variables_fecha"])
        df["años_cumplidos"] = df.apply(lambda fila: edad(fila["antropo_fnac"], fila["fecha_entr"]), axis=1)
        df["meses_cumplidos"] = df.apply(lambda fila: edad_meses(fila["antropo_fnac"], fila["fecha_entr"]), axis=1)
        return df
        
    def tabla_alimentos(self):
        variables_extra = []
        c = self.configuracion["alimentos"]
        if c["archivo_variables"]:
            t = TablaConVariable(c["archivo_variables"]["archivo_nombre"],c["archivo_variables"]["variable_variable"],c["archivo_variables"]["variable_condicion"], delimitador="|")
            variables_extra = t.variables()
        l = Lector(self.archivo_alimentos)
        df = l.extracto_variables(c["variables"]+variables_extra, variables_fecha=c["variables_fecha"])
        return df