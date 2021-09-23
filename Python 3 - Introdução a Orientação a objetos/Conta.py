class Conta:

    def __init__(self, agencia, numero, titular, saldo):
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    def sacar(self, valor):
        if(valor <= self.saldo):
            self.saldo -= valor
        else:
            print("Você não possui saldo suficiente.")
    
    def depositar(self, valor):
        self.saldo += valor
    
    def transferir(self, valor, contaDestino):
        self.sacar(valor)
        contaDestino.depositar(valor)
    
    @staticmethod
    def codigo_banco():
        return "597"

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def agencia(self):
        return self.__agencia
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    