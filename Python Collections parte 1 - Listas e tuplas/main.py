from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

conta_1 = ContaCorrente(15)
conta_1.deposita(500)
conta_2 = ContaPoupanca(24)
conta_2.deposita(350)

lista = [conta_1, conta_2]

for conta in lista:
    # print(conta)
    conta.taxas_mensais()
    # print(f'Conta depois das taxas mensais: {conta}')

conta_3 = ContaPoupanca(24)
conta_3.deposita(900)

# print(conta_3 == conta_2)

conta_4 = ContaCorrente(24)
conta_4.deposita(741)

# print(conta_3 == conta_4)

lista.extend([conta_3,conta_4])

for conta in sorted(lista, reverse=True):
    print(conta)

print(conta_1 <= conta_4)