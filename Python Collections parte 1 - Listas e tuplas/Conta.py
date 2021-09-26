from abc import ABCMeta, abstractmethod

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