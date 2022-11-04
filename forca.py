def jogar():

    print("********************************")
    print("Bem vindo ao jogo de forca!")
    print("********************************")

    palavra_secreta = "python".upper()
    letras_acertadas = ["_" for letra in palavra_secreta] # List

    print(letras_acertadas)

    acertou = False
    enforcou = False
    erros = 0

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
        acertou = "_" not in palavra_secreta
        print(letras_acertadas)

    if(acertou):
        print()
    else:
        print()

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()