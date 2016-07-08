#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import *
import Level
from Level import *

LW = 10
LH = 20
DISPLAY = (POINTSZ * LW, POINTSZ * LH)
BACKGROUND_COLOR = "#004400"

def main():
    pygame.init() # Инициация PyGame, обязательная строчка 
    timer = pygame.time.Clock()
    screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
    pygame.display.set_caption("Tetris") # Пишем в шапку
    bg = Surface(DISPLAY) # Создание видимой поверхности
                                         # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом

    lev = Level(LW, LH)
    fig = Figure()
    dt = 0

    while 1: # Основной цикл программы
        dt =  dt + timer.tick(60)
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == QUIT:
                raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_LEFT:
                fig.move(-1, 0)
            if e.type == KEYDOWN and e.key == K_RIGHT:
                fig.move(1, 0)
            if e.type == KEYDOWN and e.key == K_UP:
                fig.rotate()
        if dt > 1000:
            fig.move(0, 1)
            dt = 0
        screen.blit(bg, (0,0))      # Каждую итерацию необходимо всё перерисовывать 
        if lev.update(fig):
            del fig
            fig = Figure()
        lev.draw(screen)
        fig.draw(screen)
        pygame.display.update()     # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()
