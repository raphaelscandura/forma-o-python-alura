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
        if(self._tem_dinheiro(valor_lance)):
            raise ValueError(
                "O usuário não possui dinheiro suficiente na carteira para bancar um lance deste valor")
        else:
            lance_valido = Lance(self, valor_lance)
            leilao.adicionar_lance(lance_valido)
            return lance_valido
    
    def _tem_dinheiro(self, valor_lance):
        return valor_lance > self.carteira

class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    @property
    def lances(self):
        return self.__lances[:]

    def adicionar_lance(self, lance):
        if self._lance_valido(lance):
            if self._lista_de_lances_vazia():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor
            self.__lances.append(lance)
        else:
            raise ValueError("Erro: Lance inválido")

    def imprimir_todos_os_lances(self):
        for lance in self.__lances:
            print(
                f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

    def imprimir_maior_e_menor_lances(self):
        print(
            f'O maior lance foi de {self.maior_lance} e o menor lance foi de {self.menor_lance}')

    def ultimo_lance(self):
        return self.__lances[-1]

    def _lance_valido(self, lance):
        return self._lista_de_lances_vazia() or self._usuarios_diferentes(lance) and self._lance_maior_que_anterior(lance)

    def _lista_de_lances_vazia(self):
        return not self.__lances

    def _usuarios_diferentes(self, lance):
        return self.ultimo_lance().usuario != lance.usuario

    def _lance_maior_que_anterior(self, lance):
        return lance.valor > self.ultimo_lance().valor
