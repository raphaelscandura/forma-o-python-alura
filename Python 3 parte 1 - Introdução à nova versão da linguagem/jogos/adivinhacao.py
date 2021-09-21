import random

print("Bem vindo ao jogo de adivinhação!!!")

dificuldade = int(input(
    "Selecione a sua dificuldade: \n 1-Fácil(0-50) \n 2-Médio(0-100) \n 3-Difícil(0-200) \n"))

if(dificuldade == 1):
    numero_secreto = random.randrange(1, 51)
elif(dificuldade == 2):
    numero_secreto = random.randrange(1, 101)
else:
    numero_secreto = random.randrange(1, 201)

acertou = False
pontuacao = 1000

while(acertou != True):
    palpite = int(input("Digite o seu palpite do número secreto: "))

    if(palpite == numero_secreto):
        print("Parabéns, você acertou e fez {} pontos".format(pontuacao))
        acertou = True
    elif(palpite > numero_secreto):
        print("O seu palpite foi MAIOR do que o número secreto!")
        pontuacao -= palpite - numero_secreto
    else:
        print("O seu palpite foi MENOR do que o número secreto!")
        pontuacao -= numero_secreto - palpite

#total_de_tentativas = 5

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
