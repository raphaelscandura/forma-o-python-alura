def depositar(conta, valor):
        novo_saldo = conta[1] + valor
        codigo = conta[0]
        return (codigo, novo_saldo)

conta_1 = ("Raphael", 1400)
conta_2 = ("Bruna", 4230)

conta_1 = depositar(conta_1, 152)
print(conta_1)

