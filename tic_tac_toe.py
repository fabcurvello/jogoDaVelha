import random

# todo: REGRAS E PENDÊNCIAS A FAZER
# todo: 1 - Perguntar ao usuário quem começa o jogo (computador ou usuário)
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


def jogada():
    global vez
    if (vez == 1):
        input("\nJOGADA DO COMPUTADOR: Está pronto para isso? (pressione <ENTER>)")
        sorteio(computador)
        vez = 2
    else:
        input("\nJOGADA DO USUÁRIO: Está pronto para isso? (pressione <ENTER>)")
        sorteio(usuario)
        vez = 1


def sorteio(jogador):
    sorteado = random.randint(0, 8)
    if tabuleiro[sorteado] == " ":
        tabuleiro[sorteado] = jogador
        exibir_tabuleiro()
    else:
        print("----- MAIS UMA VEZ -----")  # todo: REMOVER FUTURAMENTE ESSA LINHA
        sorteio(jogador)


# todo: Função apenas para testes. Será melhorada conforme taferas descritas nos comentários iniciais
while True:
    jogada()
