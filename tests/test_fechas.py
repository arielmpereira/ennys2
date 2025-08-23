from datetime import date
from unittest import TestCase

from herramientas.fechas import edad

class TestModulo(TestCase):
    def test_edad_mismo_dia(self):
        self.assertEqual(0, edad(date(2020,3,20), date(2020,3,20)))

    def test_edad_mismo_mes_dia_antes(self):
        self.assertEqual(0, edad(date(2020,3,20), date(2021,3,18)))
    
    def test_edad_mismo_mes_dia_igual(self):
        self.assertEqual(1, edad(date(2020,3,20), date(2021,3,20)))

    def test_edad_mismo_mes_dia_despues(self):
        self.assertEqual(1, edad(date(2020,3,20), date(2021,3,21)))