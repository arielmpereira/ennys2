from ennys2.tablas import Tablas
from ennys2.parametricas_apareadas import MediaPesoMujeresAdultas
import logging
import sys

def configuracion():
    
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)


def analisis():
    tablas = Tablas("./data/ENNyS2_encuesta.csv", 
                    "./data/Base_Alimentos_Bebidas_Suplementos.csv", 
                    "./refdata/config.json")
    
    encuesta = tablas.tabla_encuesta()
    print(encuesta.head())


    MediaPesoMujeresAdultas(encuesta).analisis()
    
if __name__ == "__main__":
    configuracion()
    analisis()