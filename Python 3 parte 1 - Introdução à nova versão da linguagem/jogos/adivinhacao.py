print("Bem vindo ao jogo de adivinhação!!!")

numero_secreto = 42
total_de_tentativas = 5

# for rodada in range(1,total_de_tentativas +1):
#     print("Rodada {} de {}".format(rodada, total_de_tentativas))
#     palpite = int(input("Digite o seu palpite do número secreto: "))

#     if(palpite == numero_secreto):
#         print("Parabéns, você acertou!!")
#         break
#     elif(palpite > numero_secreto):
#         print("O seu palpite foi MAIOR do que o número secreto!")
#     else:
#         print("O seu palpite foi MENOR do que o número secreto!")

rodada = 1

while(rodada <= total_de_tentativas):
    print("Rodada {} de {}".format(rodada, total_de_tentativas))
    palpite = int(input("Digite o seu palpite do número secreto (entre 0 e 100): "))

    if(palpite < 1 or palpite > 100):
        print("Palpite inválido! Por favor, digite um número de 0 a 100")
        continue

    if(palpite == numero_secreto):
        print("Parabéns, você acertou!!")
        break
    elif(palpite > numero_secreto):
        print("O seu palpite foi MAIOR do que o número secreto!")
    else:
        print("O seu palpite foi MENOR do que o número secreto!")
    rodada += 1
