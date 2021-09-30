class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances
    
    def adicionar_lance(self, lance):
        self.__lances.append(lance)

    def imprimir_lances(self):
        for lance in self.__lances:
            print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')
