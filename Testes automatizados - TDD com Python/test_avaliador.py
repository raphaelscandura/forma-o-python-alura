from unittest import TestCase
from dominio import Usuario, Avaliador, Lance, Leilao


class TestAvaliador(TestCase):

    def setUp(self):
        self.pedro = Usuario("Pedro")
        self.gabriel = Usuario("Gabriel")

        self.lance_do_pedro = Lance(self.pedro, 150.0)
        self.lance_do_gabriel = Lance(self.gabriel, 100.0)

        self.leilao = Leilao("Televisão")

    def test_retorna_o_menor_e_o_maior_lance_quando_os_lances_forem_dados_em_ordem_crescente(self):
        self.leilao.adicionar_lance(self.lance_do_gabriel)
        self.leilao.adicionar_lance(self.lance_do_pedro)

        self.avaliador = Avaliador()
        self.avaliador.avalia(self.leilao)
        
        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, self.avaliador.maior_lance)

    def test_retorna_o_menor_e_o_maior_lance_quando_os_lances_forem_dados_em_ordem_decrescente(self):
        self.leilao.adicionar_lance(self.lance_do_pedro)
        self.leilao.adicionar_lance(self.lance_do_gabriel)

        self.avaliador = Avaliador()
        self.avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, self.avaliador.maior_lance)
    
    def test_retorna_o_mesmo_valor_para_maior_e_menor_lance_quando_o_leilao_so_tiver_um_lance(self):
        self.leilao.adicionar_lance(self.lance_do_pedro)

        self.avaliador = Avaliador()
        self.avaliador.avalia(self.leilao)

        valor_lance_esperado = 150.0

        self.assertEqual(valor_lance_esperado, self.avaliador.menor_lance)
        self.assertEqual(valor_lance_esperado, self.avaliador.maior_lance)
    
    def test_retorna_o_menor_e_o_maior_lance_para_mais_de_dois_lances(self):
        lola = Usuario("Lola")
        lance_da_lola = Lance(lola, 20.0)
        self.leilao.adicionar_lance(self.lance_do_gabriel)
        self.leilao.adicionar_lance(self.lance_do_pedro)
        self.leilao.adicionar_lance(lance_da_lola)

        self.avaliador = Avaliador()
        self.avaliador.avalia(self.leilao)

        menor_valor_esperado = 20.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, self.avaliador.maior_lance)