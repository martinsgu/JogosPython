import random


def jogar():

    imprimir_mensagem_inicial()

    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = inicializar_letras_acertadas(palavra_secreta) #envia o parâmentro palavra_secreta

    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while(not acertou and not enforcou):

        chute = pedir_chute()

        if(chute in palavra_secreta):
            marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenhar_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprimir_mensagem_ganhou()
    else:
        imprimir_mensagem_perdeu(palavra_secreta)


def imprimir_mensagem_inicial():
    print("********************************")
    print("Bem vindo ao jogo de forca!")
    print("********************************")

def carregar_palavra_secreta():
    palavras = []
    with open("palavras.txt", "r") as arquivo: # arquivo = open("palavras.txt", "r") - código - arquivo.close()

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return  palavra_secreta

def inicializar_letras_acertadas(palavra): #define o parâmetro palavra_secreta que na função é chamado de palavra
    return ["_" for letra in palavra] # List

def pedir_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()  # Remove spaces and turns to upper case
    return chute

def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
def desenhar_forca(erros):
        print("  _______     ")
        print(" |/      |    ")

        if (erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if (erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if (erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if (erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if (erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()
def imprimir_mensagem_ganhou():
    print("Parabéns, você acertou as letras e fugiu da forca!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def imprimir_mensagem_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(" ")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__ == "__main__"):
    jogar()