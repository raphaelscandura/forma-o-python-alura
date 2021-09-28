from validate_docbr import CPF

class Cpf:
    def __init__(self, cpf):
        documento = str(cpf)
        if(self.valida_cpf(documento)):
            self._cpf = documento
        else:
            raise ValueError("CPF Inválido!")
    
    def valida_cpf(self, documento):
        cpf = CPF()
        return cpf.validate(documento)

    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self._cpf)

    def __str__(self):
        return self.formata_cpf()