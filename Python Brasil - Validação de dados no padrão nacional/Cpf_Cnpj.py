from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self._tipo_documento = tipo_documento
        if (tipo_documento == "cpf"):
            cpf = str(documento)                
            if(self.valida_cpf(cpf)):
                self._cpf = cpf
            else:
                raise ValueError("CPF Inválido!")
        elif (tipo_documento == "cnpj"):
            cnpj = str(documento)
            if(self.valida_cnpj(cnpj)):
                self._cnpj = cnpj
            else:
                raise ValueError("CNPJ Inválido!")
        else:
            raise ValueError("Documento inválido!")

    def valida_cpf(self, cpf):
        documento = CPF()
        return documento.validate(cpf)

    def valida_cnpj(self, cnpj):
        documento = CNPJ()
        return documento.validate(cnpj)

    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self._cpf)
    
    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self._cnpj)

    def __str__(self):
        if(self._tipo_documento == "cpf"):
            return self.formata_cpf()
        elif(self._tipo_documento == "cnpj"):
            return self.formata_cnpj()