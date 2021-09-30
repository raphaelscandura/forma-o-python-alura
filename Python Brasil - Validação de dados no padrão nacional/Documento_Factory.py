from Cpf import Cpf
from Cnpj import Cnpj

class DocumentoFactory:

    def cria_documento(documento):
        if (len(documento) == 11):
            return Cpf(documento)
        elif (len(documento) == 14):
            return Cnpj(documento)
        else:
            raise ValueError("Quantidade de digitos incorreta!")