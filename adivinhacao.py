def jogar():

    import random

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("* Faça 3 mil pontos para vencer *")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)

    total_de_tentativas = 0
    rodada_atual = 1

    pontos_rodada = 1000
    pontos_total = 0
    faltante = 3000
    meta_de_pontos = 3000

    status = "perdeu"

    print("Qual nível de dificuldade?")
    print("(1)Fácil  (2)Médio  (3)Difícil")

    nivel = int(input("Digite o nível: "))

    nivel_correto = False

    if (nivel == 1 or nivel == 2 or nivel == 3):
        nivel_correto = True

    while(nivel_correto == False):
        print("Valor inválido")
        nivel = int(input("Digite o nível: "))
        if (nivel == 1 or nivel == 2 or nivel == 3):
            nivel_correto = True
        else:
            nivel_correto = False

    if(nivel == 1):
        total_de_tentativas = 20
        print("***********")
        print("* Nível {} *".format(nivel))
        print("***********")

    elif(nivel == 2):
        total_de_tentativas = 10
        print("***********")
        print("* Nível {} *".format(nivel))
        print("***********")

    elif(nivel == 3):
        total_de_tentativas = 5
        print("***********")
        print("* Nível {} *".format(nivel))
        print("***********")

    while(faltante > 0):

        numero_secreto = random.randrange(1, 101)

        if (rodada_atual == total_de_tentativas + 1):
            break
        else:
            for rodada_atual in range(1, total_de_tentativas + 1):

                faltante = 3000

                print("Tentativa {} de {}".format(rodada_atual, total_de_tentativas))

                chute_str = input("Digite um número(entre 1 e 100): {}")
                chute = int(chute_str)

                print("Você digitou {}".format(chute))

                if(chute > 100 or chute < 1):
                    print("Você deve digitar um número entre 1 e 100")
                    continue

                acertou = numero_secreto == chute
                maior = chute > numero_secreto

                if(acertou):
                    pontos_total += pontos_rodada
                    faltante -= pontos_total

                    print(  "Fim da rodada! Você acertou e fez {} pontos!".format(pontos_rodada))

                    if (faltante < 0):
                        faltante = 0

                    print("*************************************")
                    print(  "Pontuação total: {}    Faltam: {}".format(pontos_total, faltante))
                    print("*************************************")

                    break
                else:
                    if(maior):
                        print("Você errou! Você chutou acima do número secreto")
                    else:
                        print("Você errou! Você chutou abaixo do número secreto")

                    pontos_perdidos = abs(numero_secreto - chute)
                    pontos_rodada -= pontos_perdidos


                rodada_atual += 1

    faltante -= pontos_total

    if (pontos_total >= meta_de_pontos):
        status = "ganhou"

    if(status == "ganhou"):
        print("*******************************************")
        print(" Fim do jogo! Você ganhou com {} pontos!".format(pontos_total))
        print("*******************************************")
    else:
        print("***************************************************")
        print(" Fim do jogo! Você perdeu e faltaram {} pontos.".format(faltante))
        print("***************************************************")

    print("                ")
    print('"1" para sim ou "0" para não')
    jogar_novamente = int(input("Deseja jogar novamente? "))
    print("                ")

    resposta_correta = False

    if (jogar_novamente == 1 or jogar_novamente == 0):
        resposta_correta = True

    while (resposta_correta == False):
        print("Valor inválido")
        jogar_novamente = int(input("Deseja jogar novamente? "))

        if (jogar_novamente == 1 or jogar_novamente == 0):
            resposta_correta = True
        else:
            resposta_correta = False


    if(jogar_novamente == 1):
        jogar()
    elif(jogar_novamente == 0):
        print("*******************")
        print("Obrigado por jogar!")
        print("*******************")


if(__name__ == "__main__"):
    jogar()