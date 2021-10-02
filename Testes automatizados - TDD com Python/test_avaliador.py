from unittest import TestCase
from dominio import Usuario, Avaliador, Lance, Leilao


class TestAvaliador(TestCase):

    def test_avalia(self):
        pedro = Usuario("Pedro")

        gabriel = Usuario("Gabriel")

        lance_do_pedro = Lance(pedro, 150.0)
        lance_do_gabriel = Lance(gabriel, 100.0)

        leilao = Leilao("Televisão")

        leilao.adicionar_lance(lance_do_pedro)
        leilao.adicionar_lance(lance_do_gabriel)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
