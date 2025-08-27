from pandas import DataFrame
from scipy.stats import normaltest
import logging

class PruebaNormalidad:
    def __init__(self, df: DataFrame, variable: str):
        self.series = df[variable]
        
    def es_normal(self):
        return self._dagostino_pearson()
    
    def _dagostino_pearson(self):
        res = normaltest(self.series)
        logging.debug(
            "[%s] D’Agostino and Pearson’s (estadístico, p-value)=%s", 
            self.__class__.__name__, 
            res)
        return res.pvalue > 0.01
    
class MediaPesoMujeresAdultas:
    def __init__(self, df: DataFrame):
        self.df = df
        
    def analisis(self):
        adultas = self.df[(self.df["años_cumplidos"]>18)&(self.df["antropo_sex"]=="mujer")&(self.df["PESO"].notna())]
        logging.info("[%s] Normalidad peso mujeres adultas = %s", 
                     self.__class__.__name__,
                     "Si" if PruebaNormalidad(adultas, "PESO").es_normal() else "No")