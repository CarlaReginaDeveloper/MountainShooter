#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys

from my_code.menu import Menu, MENU_OPTION
from my_code.const import WIN_HEIGHT, WIN_WIDTH
from my_code.level import Level
from my_code.score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):   
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:
                score.show() 
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit() # End pygame (fechar pygame)
            else:
                pygame.quit() # Close window (fechar janela) 
                sys.exit() 
            



           