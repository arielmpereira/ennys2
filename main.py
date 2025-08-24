from ennys2.tablas import Tablas

def analisis():
    tablas = Tablas("./data/ENNyS2_encuesta.csv", 
                    "./data/Base_Alimentos_Bebidas_Suplementos.csv", 
                    "./refdata/config.json")
    
    encuesta = tablas.tabla_encuesta()
    # print(encuesta.shape)
    print(encuesta.head())


    alimentos = tablas.tabla_alimentos()
    # print(alimentos.shape)
    print(alimentos.head())

if __name__ == "__main__":
    analisis()