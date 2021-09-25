import re

class ExtratorCEP:
    def __init__(self, endereco):
        self._endereco = endereco

    def extrai_cep(self):
        pattern = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
        busca = pattern.search(self._endereco)
        if busca:
            cep = busca.group()
            return cep
        else:
            print("O CEP não foi encontrado no endereço fornecido")
