from datetime import date
from unittest import TestCase

from herramientas.fechas import edad, edad_meses

class TestModulo(TestCase):
    def test_edad_mismo_dia(self):
        self.assertEqual(0, edad(date(2020,3,20), date(2020,3,20)))

    def test_edad_mismo_mes_dia_antes(self):
        self.assertEqual(0, edad(date(2020,3,20), date(2021,3,18)))
    
    def test_edad_mismo_mes_dia_igual(self):
        self.assertEqual(1, edad(date(2020,3,20), date(2021,3,20)))

    def test_edad_mismo_mes_dia_despues(self):
        self.assertEqual(1, edad(date(2020,3,20), date(2021,3,21)))

    def test_edad_meses_bb_rn(self):
        self.assertEqual(0, edad_meses(date(2020,3,20), date(2020,4,19)))

    def test_edad_meses_bb_exacto(self):
        self.assertEqual(1, edad_meses(date(2020,3,20), date(2020,4,20)))

    def test_edad_meses_bb_fraccion(self):
        self.assertEqual(1, edad_meses(date(2020,3,20), date(2020,4,21)))

    def test_edad_meses_mayor_1_anio(self):
        self.assertEqual(13, edad_meses(date(2020,3,20), date(2021,4,21)))

    def test_edad_meses_casi_6(self):
        self.assertEqual(71, edad_meses(date(2012,10,10), date(2018,9,20)))