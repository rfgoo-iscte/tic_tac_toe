import pygame as pg
import time

pg.init()

# basico do ecrã
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("jogo do galo")
screen.fill((255, 223, 211))

pg.draw.line(screen, (0, 0, 0), (267, 50), (267, 550), 10)
pg.draw.line(screen, (0, 0, 0), (267 + 267, 50), (267 + 267, 550), 10)
pg.draw.line(screen, (0, 0, 0), (50, 200), (750, 200), 10)
pg.draw.line(screen, (0, 0, 0), (50, 400), (750, 400), 10)
myfont = pg.font.SysFont("monospace", 20)

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


# desenhar no ecra com base no user e no local


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
    if x < 267 and y < 200:
        return 1
    elif 267 < x < 267 + 267 and y < 200:
        return 2
    elif x > 2 * 267 and y < 200:
        return 3
    elif x < 267 and 200 < y < 400:
        return 4
    elif 2 * 267 > x > 267 and 200 < y < 400:
        return 5
    elif x > 2 * 267 and 200 < y < 400:
        return 6
    elif x < 267 and y > 400:
        return 7
    elif 2 * 267 > x > 267 and y > 400:
        return 8
    elif x > 2 * 267 and y > 400:
        return 9


# ação com base no click
def mouse_click(cont):
    x = pg.mouse.get_pos()[0]
    y = pg.mouse.get_pos()[1]
    lugar = place(x, y)
    desenhar(lugar, cont)


cont = True


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
    for pos in jogo:
        if pos == '':
            return False
    return True


# game loop
running = True
while running:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            running = False
        if i.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())
            if not cont:
                label = myfont.render("Jogador 1", True, (0, 0, 0), (255, 223, 211))
                screen.blit(label, (350, 10))
            else:
                label = myfont.render("Jogador 2", True, (0, 0, 0), (255, 223, 211))
                screen.blit(label, (350, 10))
            if jogo[place(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]) - 1] == '':
                mouse_click(cont)
                if igualdade():
                    if cont:
                        print("jogador 1 ganhou")

                        label = myfont.render("Jogador 1 Ganhou", True, (0, 0, 0), (255, 223, 211))
                        screen.blit(label, (350, 10))
                        pg.display.update()
                        time.sleep(2.5)
                        running = False
                    elif not cont:
                        label = myfont.render("Jogador 2 Ganhou", True, (0, 0, 0), (255, 223, 211))
                        screen.blit(label, (350, 10))
                        pg.display.update()
                        print("jogador 2 ganhou")

                        time.sleep(2.5)
                        running = False
                elif empate():
                    label = myfont.render("Empate   ", True, (0, 0, 0), (255, 223, 211))
                    screen.blit(label, (350, 10))
                    pg.display.update()
                    time.sleep(2.5)
                    print("empate")
                    running = False
                cont = not cont
