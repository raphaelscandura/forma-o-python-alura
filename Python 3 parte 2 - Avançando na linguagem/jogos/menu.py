import forca
import adivinhacao

def inicia_menu():

    escolha_valida = False

    while(not escolha_valida):
        escolha_do_usuario = int(input("Qual jogo você gostaria de jogar?\n1-Adivinhação\n2-Jogo da Forca\nDigite sua escolha: "))
        if(escolha_do_usuario == 1):
            adivinhacao.jogar_adivinhacao()
            escolha_valida = True
        elif(escolha_do_usuario == 2):
            forca.jogar_forca()
            escolha_valida = True
        else:
            print("Escolha inválida!")
if(__name__ == "__main__"):
    inicia_menu()