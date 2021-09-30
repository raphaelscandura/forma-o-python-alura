from validate_docbr import CPF, CNPJ

class Cnpj:
    def __init__(self, documento):
        cnpj = str(documento)
        if(self.valida_cnpj(cnpj)):
            self._cnpj = cnpj
        else:
            raise ValueError("CNPJ Inválido!")    

    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self._cnpj)

    def valida_cnpj(self, cnpj):
        documento = CNPJ()
        return documento.validate(cnpj)

    def __str__(self):
        return self.formata_cnpj()