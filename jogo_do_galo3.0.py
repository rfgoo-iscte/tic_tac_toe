import os
import time
import math

jogo = [
        ' ',
        ' ',
        ' ',
        ' ',
        ' ',
        ' ',
        ' ',
        ' ',
        ' '
    ]

clear = lambda: os.system('clear')


def game():
    print(" "+jogo[0]+" | "+jogo[1]+" | "+jogo[2]+" ")
    print("---|---|---")
    print(" "+jogo[3]+" | "+jogo[4]+" | "+jogo[5]+" ")
    print("---|---|---")
    print(" "+jogo[6]+" | "+jogo[7]+" | "+jogo[8]+" ")


fim = False
ganhador = -1


def winner():
    if (jogo[0] == jogo[1] == jogo[2] and jogo[0] == 'X') or \
            (jogo[3] == jogo[4] == jogo[5] and jogo[3] == 'X') or \
            (jogo[6] == jogo[7] == jogo[8] and jogo[6] == 'X') or \
            (jogo[0] == jogo[3] == jogo[6] and jogo[0] == 'X') or \
            (jogo[1] == jogo[4] == jogo[7] and jogo[1] == 'X') or \
            (jogo[2] == jogo[5] == jogo[8] and jogo[2] == 'X') or \
            (jogo[0] == jogo[4] == jogo[8] and jogo[0] == 'X') or \
            (jogo[2] == jogo[4] == jogo[6] and jogo[2] == 'X'):
        return 1

    elif (jogo[0] == jogo[1] == jogo[2] and jogo[0] == 'O') or \
            (jogo[3] == jogo[4] == jogo[5] and jogo[3] == 'O') or \
            (jogo[6] == jogo[7] == jogo[8] and jogo[6] == 'O') or \
            (jogo[0] == jogo[3] == jogo[6] and jogo[0] == 'O') or \
            (jogo[1] == jogo[4] == jogo[7] and jogo[1] == 'O') or \
            (jogo[2] == jogo[5] == jogo[8] and jogo[2] == 'O') or \
            (jogo[0] == jogo[4] == jogo[8] and jogo[0] == 'O') or \
            (jogo[2] == jogo[4] == jogo[6] and jogo[2] == 'O'):
        return -1
    elif empate():
        return 0


def empate():
    for i in jogo:
        if i == ' ':
            return False
    return True


def make_best_move(ai, jogo):
    bestScore = -math.inf
    bestMove = -math.inf

    for move in range(9):
        if jogo[move] != 'X' and jogo[move] != 'O':

            jogo[move] = 'O'
            score = minimax(ai, jogo)
            jogo[move] = ' '

            if score > bestScore:
                bestScore = score
                bestMove = move

    jogo[bestMove] = 'O'
    return


def minimax(isMaxTurn, jogo):

    if winner() == 1:
        return -1
    elif winner() == -1:
        return 1
    elif winner() == 0:
        return 0

    if isMaxTurn:

        bestScore = -math.inf
        for i in range(9):

            if jogo[i] == ' ':
                jogo[i] = 'O'
                score = minimax(False, jogo)
                jogo[i] = ' '

                if score > bestScore:
                    bestScore = score

        return bestScore

    else:
        bestScore = math.inf

        for i in range(9):

            if jogo[i] == ' ':
                jogo[i] = 'X'
                score = minimax(True, jogo)
                jogo[i] = ' '

                if score < bestScore:
                    bestScore = score

        return bestScore


while not fim:

    print("----Sua vez----")
    game()

    vez = True
    while vez:
        print("Digite a sua jogada: ")
        jogada = int(input())
        if not (1 <= jogada <= 9):
            print("O número deve ser entre 1 e 9.")

        elif jogo[jogada-1] == ' ':
            jogo[jogada-1] = 'X'
            vez = not vez
    game()
    clear()

    if winner() == 1:
        clear()
        game()
        print("Jogador 1 Ganhou")
        time.sleep(1.5)
        break
    elif winner() == 0:
        clear()
        game()
        print("Empate")
        time.sleep(1.5)
        break

    # computador joga

    make_best_move(False, jogo)
    if winner() == -1:
        clear()
        game()
        print("Computador ganhou")
        time.sleep(1.5)
        break
