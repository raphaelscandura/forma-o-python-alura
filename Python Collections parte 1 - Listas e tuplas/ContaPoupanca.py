from Conta import Conta

class ContaPoupanca(Conta):
    def taxas_mensais(self):
        self._saldo *= 1.01
        self._saldo -= 3