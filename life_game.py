'''生命游戏'''
# -*- coding: utf-8 -*-
#
# @author Epsirom

import os
from game_map import GameMap


class LifeGame(object):
    '''生命游戏'''

    def __init__(self, map_rows=10, map_cols=10, life_init_possibility=0.5):
        self.game_map = GameMap(map_rows, map_cols)
        self.game_map.reset(life_init_possibility)

    def print_map(self):
        '''打印结果'''
        os.system('cls' if os.name == 'nt' else 'clear')
        self.game_map.print_map()

    def game_cycle(self):
        '''生命游戏循环时的赋值'''
        nc_map = self.game_map.get_neighbor_count_map()
        for row in range(self.game_map.rows):
            for col in range(self.game_map.cols):
                nc = nc_map[row][col]
                if nc < 2 or nc > 3:
                    self.game_map.set(row, col, 0)
                elif nc == 3:
                    self.game_map.set(row, col, 1)
        self.print_map()
