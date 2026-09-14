

import unittest
from calculos import calcular_saldo
from decimal import Decimal
from calculos import calcular_saldo, convertir_importe

class TestCalcularSaldo(unittest.TestCase):
    def test_pago_parcial(self):
        self.assertEqual(calcular_saldo(1500, 600), 900)

    def test_deuda_cancelada(self):
        self.assertEqual(calcular_saldo(1000, 1000), 0)

    def test_saldo_a_favor(self):
        self.assertEqual(calcular_saldo(1000, 1200), -200)

    def test_calcula_centavos_con_decimal(self):
        resultado = calcular_saldo(
            Decimal("0.30"),
            Decimal("0.10"),
        )
        self.assertIsInstance(resultado, Decimal)
        self.assertEqual(resultado, Decimal("0.20"))



class TestConvertirImporte(unittest.TestCase):
    def test_convertir_importe_valido(self):
        resultado = convertir_importe ("1500.50")
        self.assertIsInstance(resultado, Decimal)
        self.assertEqual(resultado, Decimal("1500.50"))


    def test_Acepta_espacios(self):
        self.assertEqual(convertir_importe(" 250 "), Decimal("250"))



    def test_rechaza_negativos(self):
        with self.assertRaises(ValueError):
            convertir_importe("-10")


    def test_rechaza_texto(self):
        with self.assertRaises(ValueError):
            convertir_importe("hola")


    def test_rechaza_nan(self):
        with self.assertRaises(ValueError):
            convertir_importe("NaN")


    def test_rechaza_infinito(self):
        with self.assertRaises(ValueError):
            convertir_importe("Infinity")
