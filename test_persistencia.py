

import json
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

from persistencia import guardar_consultas


class TestGuardarConsultas(unittest.TestCase):
    def test_guarda_importes_como_texto(self):
        consultas = [
            {
                "cliente": "Cliente de prueba",
                "deuda": Decimal("1000.50"),
                "pago": Decimal("200.25"),
                "saldo": Decimal("800.25"),
            }
        ]

        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "consultas.json"

            resultado = guardar_consultas(consultas, ruta)
            self.assertTrue(resultado)

            with open(ruta, "r", encoding="utf-8") as archivo:
                guardadas = json.load(archivo)

            esperado = [
                {
                    "cliente": "Cliente de prueba",
                    "deuda": "1000.50",
                    "pago": "200.25",
                    "saldo": "800.25",
                }
            ]
            self.assertEqual(guardadas, esperado)

    def test_devuelve_false_si_no_puede_guardar(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "carpeta_inexistente" / "consultas.json"

            resultado = guardar_consultas([], ruta)

            self.assertFalse(resultado)
            self.assertFalse(ruta.exists())