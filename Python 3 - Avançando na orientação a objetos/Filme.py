from Programa import Programa

class Filme(Programa):

    def __init__(self, nome, ano, likes, duracao):
        super().__init__(nome, ano, likes)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao
    
    @duracao.setter
    def duracao(self, duracao):
        self._duracao = duracao

    def imprimir(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Duracao: {self.duracao} minutos - Likes {self.likes}')