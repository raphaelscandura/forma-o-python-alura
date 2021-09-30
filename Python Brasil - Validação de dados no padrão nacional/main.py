from Documento_Factory import DocumentoFactory
from Telefone import Telefone

cpf = DocumentoFactory.cria_documento("15316264754")
print(cpf)

cnpj = DocumentoFactory.cria_documento("35379838000112")
print(cnpj)

telefone = Telefone("05511911111111")
print(telefone)
