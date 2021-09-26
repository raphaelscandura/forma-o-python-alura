from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

conta_1 = ContaCorrente(15)
conta_1.deposita(500)
conta_2 = ContaPoupanca(24)
conta_2.deposita(350)

lista = [conta_1, conta_2]

for conta in lista:
    print(conta)
    conta.taxas_mensais()
    print(f'Conta depois das taxas mensais: {conta}')