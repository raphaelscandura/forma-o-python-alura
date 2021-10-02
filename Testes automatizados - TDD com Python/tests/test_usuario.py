import pytest
from src.dominio import Usuario, Leilao
from src.excecoes import LanceInvalido

@pytest.fixture
def usuario():
    return Usuario("trish", 50.0)

@pytest.fixture
def leilao():
    return Leilao("Televisao")

def test_o_usuario_deve_ter_dinheiro_suficiente_na_carteira_para_dar_o_lance(usuario, leilao):
    with pytest.raises(LanceInvalido):        
        usuario.da_lance(leilao, 100.0)

def test_deve_permitir_usuario_dar_lance_quando_o_lance_for_um_valor_menor_do_que_o_lance_na_carteira(usuario, leilao):
    lance_valido = usuario.da_lance(leilao, 20.0)
    assert leilao.ultimo_lance() == lance_valido

def test_deve_permitir_usuario_dar_lance_quando_o_lance_for_um_valor_igual_do_que_o_lance_na_carteira(usuario, leilao):
    lance_valido = usuario.da_lance(leilao, 50.0)
    assert leilao.ultimo_lance() == lance_valido