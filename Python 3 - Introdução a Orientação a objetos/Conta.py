class Conta:

    def __init__(self, agencia, numero, titular, saldo):
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def get_numero(self):
        return self.__numero
    
    def get_titular(self):
        return self.__titular
    
    def get_agencia(self):
        return self.__agencia
    
    def set_saldo(self, saldo):
        self.__saldo = saldo
    
    def set_agencia(self, agencia):
        self.__agencia = agencia
    
    def set_numero(self, numero):
        self.__numero = numero
    
    def set_titular(self, titular):
        self.__titular = titular
    