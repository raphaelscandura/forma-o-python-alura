from Conta import Conta

class ContaCorrente(Conta):

    def taxas_mensais(self):
        self._saldo -= 2