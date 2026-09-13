import unittest
from busquedas import buscar_consultas

class TestBuscarConsultas(unittest.TestCase):
    def setUp(self):
        self.consultas = [
            {"cliente": "Matias", "saldo": 500},
            {"cliente": "Daniel", "saldo": 900},
            {"cliente": "matias", "saldo": 750},
        ]

    def test_encuentra_todas_las_coincidencias(self):
        resultado = buscar_consultas(self.consultas, "Matias")
        esperado = [self.consultas[0], self.consultas[2]]
        self.assertEqual(resultado, esperado)

    def test_ignora_mayusculas_y_espacios(self):
        resultado = buscar_consultas(self.consultas, "  MATIAS  ")
        esperado = [self.consultas[0], self.consultas[2]]
        self.assertEqual(resultado, esperado)


    def test_nombre_inexistente(self):
        resultado = buscar_consultas(self.consultas, "Rocio")
        self.assertEqual(resultado, [])

    def test_no_busca_por_nombre_parcial_(self):
        resultado = buscar_consultas(self.consultas, "mati")
        self.assertEqual(resultado, [])
