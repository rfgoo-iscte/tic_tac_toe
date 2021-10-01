import random
import pygame as pg
import math

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("jogo do galo")
screen.fill((255, 223, 211))
myfont = pg.font.SysFont("monospace", 20)

label1 = myfont.render("1 jogador", True, (255, 255, 255), (0, 0, 0))
screen.blit(label1, (150, 250))

label2 = myfont.render("2 jogadores", True, (255, 255, 255), (0, 0, 0))
screen.blit(label2, (550, 250))

pg.display.update()


def linhas():
    screen.fill((255, 223, 211))
    pg.draw.line(screen, (0, 0, 0), (267, 50), (267, 550), 10)
    pg.draw.line(screen, (0, 0, 0), (267 + 267, 50), (267 + 267, 550), 10)
    pg.draw.line(screen, (0, 0, 0), (50, 200), (750, 200), 10)
    pg.draw.line(screen, (0, 0, 0), (50, 400), (750, 400), 10)
    label_restart = myfont.render("Recomecar", True, (255, 255, 255), (0, 0, 0))
    screen.blit(label_restart, (350, 550))
    label_exit = myfont.render("EXIT", True, (255, 255, 255), (0, 0, 0))
    screen.blit(label_exit, (600, 550))
    pg.display.update()


jogo = [
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    ''
]


def desenhar(lugar, cont):
    if cont and jogo[lugar - 1] == '':
        jogo[lugar - 1] = 'X'
        if lugar == 1:
            pg.draw.line(screen, (0, 0, 0), (60, 60), (238, 175), 8)
            pg.draw.line(screen, (0, 0, 0), (238, 60), (60, 175), 8)

        elif lugar == 2:
            pg.draw.line(screen, (0, 0, 0), (60 + 267, 60), (238 + 267, 175), 8)
            pg.draw.line(screen, (0, 0, 0), (238 + 267, 60), (60 + 267, 175), 8)

        elif lugar == 3:
            pg.draw.line(screen, (0, 0, 0), (60 + 2 * 267, 60), (238 + 2 * 267, 175), 8)
            pg.draw.line(screen, (0, 0, 0), (238 + 2 * 267, 60), (60 + 2 * 267, 175), 8)

        elif lugar == 4:
            pg.draw.line(screen, (0, 0, 0), (60, 60 + 200), (238, 175 + 200), 8)
            pg.draw.line(screen, (0, 0, 0), (238, 60 + 200), (60, 175 + 200), 8)

        elif lugar == 5:
            pg.draw.line(screen, (0, 0, 0), (60 + 267, 60 + 200), (238 + 267, 175 + 200), 8)
            pg.draw.line(screen, (0, 0, 0), (238 + 267, 60 + 200), (60 + 267, 175 + 200), 8)

        elif lugar == 6:
            pg.draw.line(screen, (0, 0, 0), (60 + 2 * 267, 60 + 200), (238 + 2 * 267, 175 + 200), 8)
            pg.draw.line(screen, (0, 0, 0), (238 + 2 * 267, 60 + 200), (60 + 2 * 267, 175 + 200), 8)

        elif lugar == 7:
            pg.draw.line(screen, (0, 0, 0), (60, 60 + 375), (238, 175 + 375), 8)
            pg.draw.line(screen, (0, 0, 0), (238, 60 + 375), (60, 175 + 375), 8)

        elif lugar == 8:
            pg.draw.line(screen, (0, 0, 0), (60 + 267, 60 + 375), (238 + 267, 175 + 375), 8)
            pg.draw.line(screen, (0, 0, 0), (238 + 267, 60 + 375), (60 + 267, 175 + 375), 8)

        elif lugar == 9:
            pg.draw.line(screen, (0, 0, 0), (60 + 2 * 267, 60 + 375), (238 + 2 * 267, 175 + 375), 8)
            pg.draw.line(screen, (0, 0, 0), (238 + 2 * 267, 60 + 375), (60 + 2 * 267, 175 + 375), 8)

        pg.display.update()

    elif not cont:
        jogo[lugar - 1] = 'O'
        if lugar == 1:
            pg.draw.circle(screen, (0, 0, 0), (140, 120), 70, 8)
        if lugar == 2:
            pg.draw.circle(screen, (0, 0, 0), (140 + 267, 120), 70, 8)
        if lugar == 3:
            pg.draw.circle(screen, (0, 0, 0), (140 + 2 * 267, 120), 70, 8)
        if lugar == 4:
            pg.draw.circle(screen, (0, 0, 0), (140, 120 + 185), 70, 8)
        if lugar == 5:
            pg.draw.circle(screen, (0, 0, 0), (140 + 267, 120 + 185), 70, 8)
        if lugar == 6:
            pg.draw.circle(screen, (0, 0, 0), (140 + 2 * 267, 120 + 185), 70, 8)
        if lugar == 7:
            pg.draw.circle(screen, (0, 0, 0), (140, 120 + 2 * 185), 70, 8)
        if lugar == 8:
            pg.draw.circle(screen, (0, 0, 0), (140 + 267, 120 + 2 * 185), 70, 8)
        if lugar == 9:
            pg.draw.circle(screen, (0, 0, 0), (140 + 2 * 267, 120 + 2 * 185), 70, 8)

        pg.display.update()


def place(x, y):
    if x < 267 and 50 < y < 200:
        return 1
    elif 267 < x < 267 + 267 and 50 < y < 200:
        return 2
    elif x > 2 * 267 and 50 < y < 200:
        return 3
    elif x < 267 and 200 < y < 400:
        return 4
    elif 2 * 267 > x > 267 and 200 < y < 400:
        return 5
    elif x > 2 * 267 and 200 < y < 400:
        return 6
    elif x < 267 and 550 > y > 400:
        return 7
    elif 2 * 267 > x > 267 and 550 > y > 400:
        return 8
    elif x > 2 * 267 and 550 > y > 400:
        return 9


def mouse_click(cont):
    x = pg.mouse.get_pos()[0]
    y = pg.mouse.get_pos()[1]
    lugar = place(x, y)
    desenhar(lugar, cont)


def igualdade():
    if (jogo[0] == jogo[1] == jogo[2] and jogo[0] != '' and jogo[1] != '' and jogo[2] != '') or \
            (jogo[3] == jogo[4] == jogo[5] and jogo[3] != '' and jogo[4] != '' and jogo[5] != '') or \
            (jogo[6] == jogo[7] == jogo[8] and jogo[6] != '' and jogo[7] != '' and jogo[8] != '') or \
            (jogo[0] == jogo[3] == jogo[6] and jogo[0] != '' and jogo[3] != '' and jogo[6] != '') or \
            (jogo[1] == jogo[4] == jogo[7] and jogo[1] != '' and jogo[4] != '' and jogo[7] != '') or \
            (jogo[2] == jogo[5] == jogo[8] and jogo[2] != '' and jogo[5] != '' and jogo[8] != '') or \
            (jogo[0] == jogo[4] == jogo[8] and jogo[0] != '' and jogo[4] != '' and jogo[8] != '') or \
            (jogo[2] == jogo[4] == jogo[6] and jogo[2] != '' and jogo[4] != '' and jogo[6] != ''):

        return True
    else:
        return False


def empate():
    for i in jogo:
        if i == '':
            return False
    return True


def make_best_move(ai, jogo):
    bestScore = -math.inf
    bestMove = -math.inf                                                                   
    for move in range(9):
        if jogo[move] != 'X' and jogo[move] != 'O':
            jogo[move] = 'O'

            score = minimax(ai, jogo)
            jogo[move] = ''
            if score > bestScore:
                bestScore = score
                bestMove = move

    #desenhar(bestMove + 1, False)
    return bestMove + 1

def minimax(isMaxTurn, jogo):
    if igualdade() and isMaxTurn:
        return -1
    elif igualdade() and not isMaxTurn:
        return 1
    elif empate():
        return 0

    if isMaxTurn:
        bestScore = -math.inf
        for i in range(9):
            if jogo[i] == '':
                jogo[i] = 'O'
                score = minimax(False, jogo)
                jogo[i] = ''

                if score > bestScore:
                    bestScore = score

        return bestScore
    else:
        bestScore = math.inf
        for i in range(9):
            if jogo[i] == '':
                jogo[i] = 'X'
                score = minimax(True, jogo)
                jogo[i] = ''
                if score < bestScore:
                    bestScore = score
        return bestScore


def final(cont, players):
    score = ""
    if igualdade():

        if cont:
            print("jogador 1 ganhou")
            labelj1 = myfont.render("Jogador 1 Ganhou", True, (0, 0, 0), (255, 223, 211))
            screen.blit(labelj1, (350, 10))
            pg.display.update()

        elif not cont:
            if players == 2:
                score = "Jogador 2 Ganhou"
            elif players == 1:
                score = "Computador ganhou"

            labelj2 = myfont.render("%s" % score, True, (0, 0, 0), (255, 223, 211))
            screen.blit(labelj2, (350, 10))
            pg.display.update()
            print(score)

    elif empate():

        labele = myfont.render("Empate   ", True, (0, 0, 0), (255, 223, 211))
        screen.blit(labele, (350, 10))
        pg.display.update()
        print("empate")
    return True


cont = True
running = True
players = 0

while running:

    for i in pg.event.get():

        if i.type == pg.QUIT:
            running = False
            
        if i.type == pg.MOUSEBUTTONUP and players == 0:

            if 150 < pg.mouse.get_pos()[0] < 260 and 250 < pg.mouse.get_pos()[1] < 270:
                players = 1
                linhas()

            elif 550 < pg.mouse.get_pos()[0] < 680 and 250 < pg.mouse.get_pos()[1] < 270:
                players = 2
                linhas()

        if i.type == pg.MOUSEBUTTONDOWN and 350 < pg.mouse.get_pos()[0] < 460 and 550 < pg.mouse.get_pos()[1] < 570:

            for o in range(9):
                jogo[o] = ''

            cont = True
            linhas()

        if i.type == pg.MOUSEBUTTONDOWN and 600 < pg.mouse.get_pos()[0] < 650 and 550 < pg.mouse.get_pos()[1] < 570:
            running = False

        if i.type == pg.MOUSEBUTTONDOWN and players != 0 and 50 < pg.mouse.get_pos()[1] < 550:
            print(pg.mouse.get_pos())

            if not cont and players == 2:
                label = myfont.render("Jogador 1", True, (0, 0, 0), (255, 223, 211))
                screen.blit(label, (350, 10))

            elif cont and players == 2:
                label = myfont.render("Jogador 2", True, (0, 0, 0), (255, 223, 211))
                screen.blit(label, (350, 10))

            if jogo[place(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]) - 1] == '' and players == 2:
                mouse_click(cont)
                running = final(cont, players)
                cont = not cont
                print("Sugestão: ", make_best_move(cont, jogo))

            elif players == 1:

                if jogo[place(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]) - 1] == '' and cont and not igualdade() and\
                        not empate():

                    mouse_click(True)
                    running = final(cont, players)
                    cont = not cont

                    if not igualdade() and not empate():
                        ran = random.randint(0,100) / 100
                        
                        if ran > 0.15:
                            desenhar(make_best_move(cont, jogo), False)
                        elif ran <= 0.15:
                            p = random.randint(1, 9)
                            while jogo[p-1] != '':
                                p = random.randint(1, 9)

                            desenhar(p, False)
                        running = final(cont, players)
                        cont = not cont
