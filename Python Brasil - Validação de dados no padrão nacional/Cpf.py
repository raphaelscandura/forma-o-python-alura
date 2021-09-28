class Cpf:
    def __init__(self, cpf):
        cpf = str(cpf)
        if(self.valida_cpf(cpf)):
            self._cpf = cpf
        else:
            raise ValueError("CPF Inválido!")
    
    def valida_cpf(self, cpf):
        if len(cpf) == 11:
            return True
        else:
            return False