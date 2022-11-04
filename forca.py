import random


def jogar():

    palavras = []

    with open("palavras.txt", "r") as arquivo: # arquivo = open("palavras.txt", "r") - código - arquivo.close()

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    print("********************************")
    print("Bem vindo ao jogo de forca!")
    print("********************************")

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta] # List

    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while(not acertou and not enforcou):

        chute = input("Qual letra?")
        chute = chute.strip().upper() # Remove spaces and turns to upper case

        if(chute in palavra_secreta):
            index = 0 # Position

            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()