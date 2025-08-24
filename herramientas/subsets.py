import pandas as pd

class TablaConVariable:
    def __init__(self, archivo_nombre, columna_variable, columna_indicador, delimitador=","):
        self.archivo_nombre = archivo_nombre
        self.columna_variable = columna_variable
        self.columna_indicador = columna_indicador
        self.delimitador = delimitador

    def variables(self):
        df = pd.read_csv(self.archivo_nombre, delimiter=self.delimitador)
        return df[df[self.columna_indicador]==True][self.columna_variable].to_list()
