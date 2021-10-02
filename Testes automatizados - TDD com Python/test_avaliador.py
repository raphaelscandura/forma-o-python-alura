from unittest import TestCase
from dominio import Usuario, Avaliador, Lance, Leilao


class TestAvaliador(TestCase):

    def test_retorna_o_menor_e_o_maior_lance_quando_os_lances_forem_dados_em_ordem_crescente(self):
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

    def test_retorna_o_menor_e_o_maior_lance_quando_os_lances_forem_dados_em_ordem_decrescente(self):
        pedro = Usuario("Pedro")

        gabriel = Usuario("Gabriel")

        lance_do_pedro = Lance(pedro, 150.0)
        lance_do_gabriel = Lance(gabriel, 100.0)

        leilao = Leilao("Televisão")

        leilao.adicionar_lance(lance_do_gabriel)
        leilao.adicionar_lance(lance_do_pedro)
        

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
    
    def test_retorna_o_mesmo_valor_para_maior_e_menor_lance_quando_o_leilao_so_tiver_um_lance(self):
        pedro = Usuario("Pedro")

        lance_do_pedro = Lance(pedro, 150.0)

        leilao = Leilao("Televisão")

        leilao.adicionar_lance(lance_do_pedro)        

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        valor_lance_esperado = 150.0

        self.assertEqual(valor_lance_esperado, avaliador.menor_lance)
        self.assertEqual(valor_lance_esperado, avaliador.maior_lance)
    
    def test_retorna_o_menor_e_o_maior_lance_para_mais_de_dois_lances(self):
        pedro = Usuario("Pedro")
        lola = Usuario("Lola")
        gabriel = Usuario("Gabriel")

        lance_do_pedro = Lance(pedro, 150.0)
        lance_da_lola = Lance(lola, 20.0)
        lance_do_gabriel = Lance(gabriel, 100.0)

        leilao = Leilao("Televisão")

        leilao.adicionar_lance(lance_do_pedro)
        leilao.adicionar_lance(lance_da_lola)
        leilao.adicionar_lance(lance_do_gabriel)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)