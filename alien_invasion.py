"""
创建pygame窗口
启动游戏的程序入口
完成各种功能函数的调用
"""

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf  # 功能函数模块


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    # 设置类实例化
    settings = Settings()
    # surface component 屏幕对象
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # 飞船实例化
    ship = Ship(screen)
    pygame.display.set_caption("Alien Invasion")   # set title

    # 开始游戏的主循环
    while True:

        gf.check_events(ship)
        ship.update()
        gf.update_screen(settings, screen, ship)

run_game()
