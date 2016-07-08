#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import *
import random

POINTSZ = 40
COLOR = "#ffffff"

class Level(sprite.Sprite):
    def __init__(self, w, h):
        sprite.Sprite.__init__(self)
        self.image = Surface((POINTSZ, POINTSZ))
        self.image.fill(Color(COLOR))
#        self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект
        self.content = [[1] * w for i in range(h)]
        self.w = w
        self.h = h
        for i in range(h):
            for j in range(w):
                if i > (h / 2):
                    self.content[i][j] = random.randint(0, 5)

    def update(self, figure):
        for i in range(4):
            for j in range(4):
                if figure.content[j][i] == 0 and self.content[figure.x + j + 1][figure.y + i] == 0:
                    apply(figure)
                    return True
        return False

    def apply(self, figure):
        for i in range(4):
            for j in range(4):
                if figure.content[i][j] == 0:
                    self.content[figure.x + i][figure.y + j] = 0


    def draw(self, screen): # Выводим себя на экран
        for i in range(self.h):
            for j in range(self.w):
                if self.content[i][j] == 0:
                    screen.blit(self.image, (j * POINTSZ, i * POINTSZ))

class Figure(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = Surface((POINTSZ, POINTSZ))
        self.image.fill(Color(COLOR))
        self.content = [[0, 1, 1, 1],
                        [0, 1, 1, 1],
                        [0, 0, 1, 1],
                        [1, 1, 1, 1]]
        self.x = 3
        self.y = 0

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def rotate(self):
        oldContent = self.content
        print "rotate"
        for i in range(4):
            for j in range(4):
                self.content[i][j] == self.content[j][i]

    def draw(self, screen): # Выводим себя на экран
        for i in range(4):
            for j in range(4):
                if self.content[i][j] == 0:
                    screen.blit(self.image, ((self.x + j) * POINTSZ, (self.y + i) * POINTSZ))

