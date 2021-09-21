print("Bem vindo ao jogo de adivinhação!!!")

numero_secreto = 42

palpite = int(input("Digite o seu palpite do número secreto: "))

if(palpite == numero_secreto):
    print("Parabéns, você acertou!!")
else:
    print("Seu palpite está ERRADO! Tente novamente!")
