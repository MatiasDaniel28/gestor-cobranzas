

import unittest
from calculos import calcular_saldo


class TestCalcularSaldo(unittest.TestCase):
    def test_pago_parcial(self):
        self.assertEqual(calcular_saldo(1500, 600), 900)

    def test_deuda_cancelada(self):
        self.assertEqual(calcular_saldo(1000, 1000), 0)

    def test_saldo_a_favor(self):
        self.assertEqual(calcular_saldo(1000, 1200), -200)