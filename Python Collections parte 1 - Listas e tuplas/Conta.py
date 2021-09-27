from functools import total_ordering
from abc import ABCMeta, abstractmethod

@total_ordering
class Conta(metaclass = ABCMeta):
    def __init__(self, codigo) -> None:
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def taxas_mensais():
        pass
    
    def __str__(self):
        return f'Código: {self._codigo} Saldo: {self._saldo}'

    def __eq__(self, outra_conta):
        if(type(self) == type(outra_conta)):
            return self._codigo == outra_conta._codigo
        else:
            return False
    
    def __lt__(self, outro):
        if(self._saldo != outro._saldo):
            return self._saldo < outro._saldo
        else:
            return self._codigo < outro._codigo