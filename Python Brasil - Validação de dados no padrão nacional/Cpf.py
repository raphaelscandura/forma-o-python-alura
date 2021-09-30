from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        cpf = str(documento)                
        if(self.valida_cpf(cpf)):
            self._cpf = cpf

    def valida_cpf(self, cpf):
        documento = CPF()
        return documento.validate(cpf)

    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self._cpf)    

    def __str__(self):
        return self.formata_cpf()