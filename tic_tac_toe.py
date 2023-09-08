import random

# todo: REGRAS E PENDÊNCIAS A FAZER
# todo: 2 - Na vez do usuário, perguntar onde ele quer jogar, de acordo com as casas vazias no tabuleiro.
# todo:   2.1 - Se ele pressionar enter ou escolher valor inválido o computador vai sortear a jogada do usuário
# todo: 3 - Detectar quando houver um vencedor e encerrar o jogo
# todo: 4 - Detecar se o tabuleiro ficar cheio e não houver vencedor e encerrar o jogo

tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
computador = "X"
usuario = "O"
vez = 1

print("-------------------------------------")
print("--- JOGO DA VELHA --- TIC-TAC-TOE ---")
print("-------------------------------------\n")

print("-------------------------------------")
print("---    JOGADOR    ---     PEÇA    ---")
print("---  Computador   ---      X      ---")
print("---     Você      ---      O      ---")
print("-------------------------------------\n")


def quem_comeca():
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
        jogada_escolha_usuario()
        # sorteio(usuario)
        vez = 2
    else:  # Vez do computador
        input("\nJOGADA DO COMPUTADOR: Está pronto para isso? (pressione <ENTER>)")
        sorteio(computador)
        vez = 1


def jogada_escolha_usuario():
    exibir_tabuleiro()
    print("Informe o número da posição no tabuleiro que você quer jogar:")
    print("OBS: Qualquer valor inválido fará o computador sortear um número para a sua jogada.")
    posicao = int(input())
    tabuleiro[posicao - 1] = "O"  # todo tratar valores válidos x inválidos
    exibir_tabuleiro()


def sorteio(jogador):
    sorteado = random.randint(0, 8)
    if tabuleiro[sorteado] == " ":
        tabuleiro[sorteado] = jogador
        exibir_tabuleiro()
    else:
        print("----- MAIS UMA VEZ -----")  # todo: REMOVER FUTURAMENTE ESSA LINHA
        sorteio(jogador)


def exibir_tabuleiro():
    print(" 1       | 2       | 3       ")
    print(f"    {tabuleiro[0]}    |    {tabuleiro[1]}    |    {tabuleiro[2]}    ")
    print("         |         |         ")
    print("---------+---------+---------")
    print(" 4       | 5       | 6       ")
    print(f"    {tabuleiro[3]}    |    {tabuleiro[4]}    |    {tabuleiro[5]}    ")
    print("         |         |         ")
    print("---------+---------+---------")
    print(" 7       | 8       | 9       ")
    print(f"    {tabuleiro[6]}    |    {tabuleiro[7]}    |    {tabuleiro[8]}    ")
    print("         |         |         ")


quem_comeca()

# todo: Função apenas para testes. Será melhorada conforme taferas descritas nos comentários iniciais
while True:
    jogada()
