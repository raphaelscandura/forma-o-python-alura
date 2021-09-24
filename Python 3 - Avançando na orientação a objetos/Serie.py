from Programa import Programa

class Serie(Programa):
    def __init__(self, nome, ano, likes, temporadas):
        super().__init__(nome, ano, likes)
        self._temporadas = temporadas

    @property
    def temporadas(self):
        return self._temporadas
    
    @temporadas.setter
    def temporadas(self, temporadas):
        self._temporadas = temporadas
    
    def imprimir(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes {self.likes}')