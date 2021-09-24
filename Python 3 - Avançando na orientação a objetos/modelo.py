class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.__ano = ano
        self.__duracao = duracao
    
    @property
    def nome(self):
        return self.__nome.title()
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao

    def imprimir(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Duracao: {self.duracao}')

class Serie:
    
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.__ano = ano
        self.__temporadas = temporadas
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    
    @property
    def temporadas(self):
        return self.__temporadas
    
    @temporadas.setter
    def temporadas(self, temporadas):
        self.__temporadas = temporadas
    
    def imprimir(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas}')