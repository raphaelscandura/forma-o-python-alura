import sys

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome
    
    @property
    def carteira(self):
        return self.__carteira
    
    def da_lance(self, leilao, valor_lance):
        if(valor_lance > self.carteira):
            raise ValueError("O usuário não possui dinheiro suficiente na carteira para bancar um lance deste valor")
        else:
            lance_valido = Lance(self,valor_lance)
            leilao.adicionar_lance(lance_valido)
            return lance_valido


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    @property
    def lances(self):
        return self.__lances[:]
    
    def adicionar_lance(self, lance):
        if not self.__lances or self.__lances[-1].usuario != lance.usuario and lance.valor > self.lances[-1].valor:
            if(self.maior_lance < lance.valor):
                self.maior_lance = lance.valor
            if(self.menor_lance > lance.valor):
                self.menor_lance = lance.valor
            self.__lances.append(lance)
        else:
            raise ValueError("Erro: Lance inválido")

    def imprimir_todos_os_lances(self):
        for lance in self.__lances:
            print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

    def imprimir_maior_e_menor_lances(self):
        print(f'O maior lance foi de {self.maior_lance} e o menor lance foi de {self.menor_lance}')

    def ultimo_lance(self):
        return self.__lances[-1]    