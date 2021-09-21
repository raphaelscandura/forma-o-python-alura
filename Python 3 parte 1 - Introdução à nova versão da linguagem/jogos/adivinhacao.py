print("Bem vindo ao jogo de adivinhação!!!")

numero_secreto = 42
total_de_tentativas = 5
rodada = 0

while(rodada <= total_de_tentativas):
    print("Rodada {} de {}".format(rodada, total_de_tentativas))
    palpite = int(input("Digite o seu palpite do número secreto: "))

    if(palpite == numero_secreto):
        print("Parabéns, você acertou!!")
        break
    elif(palpite > numero_secreto):
        print("O seu palpite foi MAIOR do que o número secreto!")
    else:
        print("O seu palpite foi MENOR do que o número secreto!")
    rodada += 1
