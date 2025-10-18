#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from my_code.menu import Menu
from my_code.const import WIN_HEIGHT, WIN_WIDTH

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        

        while True:
            menu = Menu(self.window)
            menu.run()
            pass



           