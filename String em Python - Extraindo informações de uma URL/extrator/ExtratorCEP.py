import re

class ExtratorCEP:
    def __init__(self, endereco):
        self._endereco = endereco

    def extrai_cep(self):
        pattern = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
        busca = pattern.search(self._endereco)
        if busca:
            cep = busca.group()
            return cep
        else:
            print("O CEP não foi encontrado no endereço fornecido")
