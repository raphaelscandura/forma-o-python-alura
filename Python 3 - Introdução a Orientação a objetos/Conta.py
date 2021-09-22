class Conta:

    def __init__(self, agencia, numero, titular, saldo):
        self.agencia = agencia
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def get_saldo(self):
        return self.saldo
    
    def get_numero(self):
        return self.numero
    
    def get_titular(self):
        return self.get_titular
    
    def get_agencia(self):
        return self.agencia
    
    def set_saldo(self, saldo):
        self.saldo = saldo
    
    def set_agencia(self, agencia):
        self.agencia = agencia
    
    def set_numero(self, numero):
        self.numero = numero
    
    def set_titular(self, titular):
        self.titular = titular
    