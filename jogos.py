import forca
import adivinhacao

def escolhe_jogo():

    print("********************************")
    print("****** ESCOLHA O SEU JOGO ******")
    print("********************************")

    print("(1)Forca ou (2)Adivinhação")

    jogo = int(input("Jogo escolhido: "))

    if(jogo == 1):
        print("Jogando forca!")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação!")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()