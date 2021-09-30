import re

class Telefone:

    def __init__(self, telefone):
        telefone = str(telefone)
        if (self.valida_telefone(telefone)):
            self._telefone = telefone
        else:
            raise ValueError("Número de telefone inválido")
    
    def valida_telefone(self,telefone):
        padrao = "([0-9]{1,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if (resposta):
            return True
        else:
            return False
    
    def formata_telefone(self):
        padrao = "([0-9]{1,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self._telefone)
        numero_formatado = f'+{resposta.group(1)} ({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}'
        return numero_formatado

    def __str__(self):
        return self.formata_telefone()
