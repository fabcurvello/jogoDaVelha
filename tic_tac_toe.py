import random

# todo: REGRAS E PENDÊNCIAS A FAZER
# todo: 4 - Detecar se o tabuleiro ficar cheio e não houver vencedor e encerrar o jogo

tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
computador = "X"
usuario = "O"
vez = 1  # 1 - usuário; 2 - computador
continua = True

print("-------------------------------------")
print("--- JOGO DA VELHA --- TIC-TAC-TOE ---")
print("-------------------------------------\n")

print("-------------------------------------")
print("---    JOGADOR    ---     PEÇA    ---")
print("---  Computador   ---      X      ---")
print("---     Você      ---      O      ---")
print("-------------------------------------\n")


def quem_comeca():  # 1 - usuário; 2 - computador
    print("Responda quem deve iniciar a jogada:")
    print("Digite 1 para VOCÊ iniciar;")
    print("Digite outro número para o COMPUTADOR iniciar:")
    starter = input()
    global vez
    if (starter == "1"):
        vez = 1
    else:
        vez = 2


def jogada():
    global vez
    if (vez == 1):  # Vez do usuário
        input("\nSUA JOGADA: Está pronto para isso? (pressione <ENTER>)")
        jogador = usuario
        jogada_escolha_usuario()
        vez = 2

    else:  # Vez do computador
        input("\nJOGADA DO COMPUTADOR: Está pronto para isso? (pressione <ENTER>)")
        jogador = computador
        sorteio(computador)
        vez = 1
    verifica_venceu_partida(jogador)


def jogada_escolha_usuario():
    exibir_tabuleiro()
    print("Informe o número da posição no tabuleiro que você quer jogar:")
    print("OBS: Qualquer valor inválido fará o computador sortear um número para a sua jogada.")

    try:
        posicao = int(input())
    except ValueError as erro:
        posicao = 10

    if( posicao > 9 or posicao < 1):
        print("Posição escolhida é INVÁLIDA!. Sua jogada será por sorteio.....")
        sorteio(usuario)
    elif( tabuleiro[posicao - 1] == " "):
        tabuleiro[posicao - 1] = "O"
        exibir_tabuleiro()
    else:
        print("Posição escolhida JÁ ESTÁ OCUPADA!. Sua jogada será por sorteio.....")
        sorteio(usuario)


def sorteio(jogador):
    sorteado = random.randint(0, 8)
    if tabuleiro[sorteado] == " ":
        tabuleiro[sorteado] = jogador
        exibir_tabuleiro()
    else:
        sorteio(jogador)


def exibir_tabuleiro():
    print("          +---------------------------------+")
    print("          |                                 |")
    print("          |   1       | 2       | 3         |")
    print(f"          |      {tabuleiro[0]}    |    {tabuleiro[1]}    |    {tabuleiro[2]}      |")
    print("          |           |         |           |")
    print("          |  ---------+---------+---------  |")
    print("          |   4       | 5       | 6         |")
    print(f"          |      {tabuleiro[3]}    |    {tabuleiro[4]}    |    {tabuleiro[5]}      |")
    print("          |           |         |           |")
    print("          |  ---------+---------+---------  |")
    print("          |   7       | 8       | 9         |")
    print(f"          |      {tabuleiro[6]}    |    {tabuleiro[7]}    |    {tabuleiro[8]}      |")
    print("          |           |         |           |")
    print("          |                                 |")
    print("          +---------------------------------+")


def verifica_venceu_partida(jogador):
    global continua
    vencedor = ("VOCÊ", "COMPUTADOR")[jogador == "X"]
    mensagem = f"- - - FINAL DO JOGO: {vencedor} VENCEU A PARTIDA !!! - - -"
    if ( (tabuleiro[0]==jogador) and (tabuleiro[1]==jogador) and (tabuleiro[2]==jogador) ):
        print(mensagem)
        continua = False
    elif ( (tabuleiro[3]==jogador) and (tabuleiro[4]==jogador) and (tabuleiro[5]==jogador) ):
        print(mensagem)
        continua = False
    elif ((tabuleiro[6] == jogador) and (tabuleiro[7] == jogador) and (tabuleiro[8] == jogador)):
        print(mensagem)
        continua = False
    elif ( (tabuleiro[0]==jogador) and (tabuleiro[3]==jogador) and (tabuleiro[6]==jogador) ):
        print(mensagem)
        continua = False
    elif ( (tabuleiro[1]==jogador) and (tabuleiro[4]==jogador) and (tabuleiro[7]==jogador) ):
        print(mensagem)
        continua = False
    elif ( (tabuleiro[2]==jogador) and (tabuleiro[5]==jogador) and (tabuleiro[8]==jogador) ):
        print(mensagem)
        continua = False
    elif ( (tabuleiro[0]==jogador) and (tabuleiro[4]==jogador) and (tabuleiro[8]==jogador) ):
        print(mensagem)
        continua = False
    elif ( (tabuleiro[2]==jogador) and (tabuleiro[4]==jogador) and (tabuleiro[6]==jogador) ):
        print(mensagem)
        continua = False

# EXECUÇÃO DO PROJETO:
quem_comeca()

# todo: Função apenas para testes. Será melhorada conforme taferas descritas nos comentários iniciais
while (continua):
    jogada()
