import pandas as pd
from herramientas.lector import Lector

def personas():
    l = Lector("./data/ENNyS2_encuesta.csv")
    df = l.extracto_variables(("MHDR_KEY", "E_CUEST", "region", "fecha_entr", "antropo_fnac", "antropo_sex", "PESO", "TALLA", "IMC", "ZPE", "ZTE", "PTZ", "Cobertura_salud"), variables_fecha=("fecha_entr", "antropo_fnac"))
    print("Personas:", len(df))
    print(df.head())

def alimentos():
    df = pd.read_csv("./data/Base_Alimentos_Bebidas_Suplementos.csv", low_memory=False)
    print("Alimentos:", len(df))

def nutrientes():
    df = pd.read_csv("./data/Base_Nutrientes.csv", low_memory=False)
    print("Nutrientes:", len(df))

if __name__ == "__main__":
    personas()
    alimentos()
    nutrientes()