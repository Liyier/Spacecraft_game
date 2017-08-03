"""
创建pygame窗口
启动游戏的程序入口
完成各种功能函数的调用
"""

import sys
import pygame
from settings import Settings


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))  # surface component
    pygame.display.set_caption("Alien Invasion")   # set title

    # 开始游戏的主循环
    while True:

        # 监督键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每循环一次重新填充一次屏幕
        screen.fill(settings.bg_color)
        # 让最近绘制的屏幕可见(绘制一个空屏幕，擦去旧屏幕)
        pygame.display.flip()

run_game()
