class Programa:
    def __init__(self, nome, ano, likes):
        self._nome = nome
        self._ano = ano
        self._likes = likes

    @property
    def nome(self):
        return self._nome.title()
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, ano):
        self._ano = ano

    @property
    def likes(self):
        return self._likes
    
    @likes.setter
    def likes(self, likes):
        self._likes = likes
    
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes {self.likes}'
