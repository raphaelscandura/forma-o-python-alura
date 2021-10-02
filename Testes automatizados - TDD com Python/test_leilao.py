from unittest import TestCase
from dominio import Usuario,Lance, Leilao

# Regras de negócio:
# 1 - Um usuário só pode dar um lance se ele for maior do que o lance anterior
# 2 - Um usuário não pode dar um lance seguido de outro lance dele mesmo
# 3 - Se o leilão não tiver nenhum lance, qualquer usuário pode dar um lance

class TestLeilao(TestCase):

    def setUp(self):
        self.pedro = Usuario("Pedro")
        self.gabriel = Usuario("Gabriel")

        self.lance_do_gabriel = Lance(self.gabriel, 100.0)
        self.lance_do_pedro = Lance(self.pedro, 150.0)        

        self.leilao = Leilao("Televisão")
    
    def test_deve_permitir_um_usuario_dar_o_primeiro_lance(self):
        self.leilao.adicionar_lance(self.lance_do_gabriel)

        quantidade_de_lances = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances)

    def test_deve_permitir_um_usuario_dar_um_lance_caso_nao_seja_o_mesmo_usuario_do_lance_atual(self):
        segundo_lance_do_gabriel = Lance(self.gabriel, 110.0)

        self.leilao.adicionar_lance(self.lance_do_gabriel)
        self.leilao.adicionar_lance(segundo_lance_do_gabriel)

        quantidade_de_lances = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances)
        
    def test_retorna_o_menor_e_o_maior_lance(self):
        self.leilao.adicionar_lance(self.lance_do_gabriel)
        self.leilao.adicionar_lance(self.lance_do_pedro)
        
        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    
    def test_retorna_o_mesmo_valor_para_maior_e_menor_lance_quando_o_leilao_so_tiver_um_lance(self):
        self.leilao.adicionar_lance(self.lance_do_pedro)

        valor_lance_esperado = 150.0

        self.assertEqual(valor_lance_esperado, self.leilao.menor_lance)
        self.assertEqual(valor_lance_esperado, self.leilao.maior_lance)
    
    def test_retorna_o_menor_e_o_maior_lance_para_mais_de_dois_lances(self):
        lola = Usuario("Lola")
        lance_da_lola = Lance(lola, 20.0)
        self.leilao.adicionar_lance(lance_da_lola)
        self.leilao.adicionar_lance(self.lance_do_gabriel)
        self.leilao.adicionar_lance(self.lance_do_pedro)
        

        menor_valor_esperado = 20.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)