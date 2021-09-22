import random


def jogar_forca():
    print("Bem vido ao jogo da Forca!")

    palavra_secreta = definir_palavra_secreta()

    acertou = False
    tentativas = 6
    letras_da_palavra = ["_" for letra in palavra_secreta]

    while(tentativas != 0 and not acertou):
        print(letras_da_palavra)
        palpite_letra = input(
            "Digite uma letra que você acha que tem na palavra secreta: ")
        palpite_letra_tratado = palpite_letra.strip().upper()

        if(palpite_letra_tratado in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(palpite_letra_tratado == letra):
                    letras_da_palavra[index] = letra
                index += 1
        else:   
            tentativas -= 1
        desenha_forca(tentativas)
        acertou = "_" not in letras_da_palavra

    if(acertou):
        print("Você ganhou! Parabéns")
    else:
        print("Suas tentativas acabaram, você perdeu!")

    print("Fim do jogo")

def definir_palavra_secreta():
    arquivo = open("palavras.txt", "w")
    arquivo.write("banana\n")
    arquivo.write("abacaxi\n")
    arquivo.write("arroz\n")
    arquivo.write("frango\n")

    arquivo.close()

    arquivo = open("palavras.txt", "r")

    lista = []

    for palavras in arquivo:
        palavras = palavras.strip()
        lista.append(palavras)

    arquivo.close()

    numero = random.randrange(0, len(lista))

    palavra_secreta = lista[numero].upper()

    return palavra_secreta

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 5):
        print(" |     (º-º)  ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |     (º-º)  ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 3):
        print(" |     (º-º)  ")
        print(" |      \|    ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 2):
        print(" |     (º-º)  ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 1):
        print(" |     (º-º)  ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 0):
        print(" |     (º-º)  ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if(__name__ == "__main__"):
    jogar_forca()
