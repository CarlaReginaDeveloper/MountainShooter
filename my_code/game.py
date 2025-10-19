#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from my_code.menu import Menu, MENU_OPTION
from my_code.const import WIN_HEIGHT, WIN_WIDTH
from my_code.level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):   
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[3]:
                pass 
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit() # End pygame (fechar pygame)
            else:
                pygame.quit() # Close window (fechar janela) 
                exit() 
            



           