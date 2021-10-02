import sys

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