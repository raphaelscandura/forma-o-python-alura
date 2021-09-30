import requests

class Endereco:

    def __init__(self,cep):
        cep = str(cep)
        if(self.valida_cep(cep)):
            self._endereco = self.busca_endereco(cep)
        else:
            raise ValueError("CEP Inválido!")

    def valida_cep(self, cep):
        if(len(cep) == 8):
            return True
        else:
            return False

    def busca_endereco(self, cep):
        r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        return r.json()

    def __str__(self):
        return f'{self._endereco["logradouro"]}, {self._endereco["complemento"]}, {self._endereco["bairro"]} - {self._endereco["localidade"]}, {self._endereco["uf"]}'