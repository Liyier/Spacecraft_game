"""
该项目游戏中的ship
将imgae的rect放置在整个游戏屏幕的screen的rect中
pygame 处理rect(矩形)一样处理游戏元素
rect对象有center(估计是元组),centerx,centery等属性
"""
import pygame


class Ship(object):

    def __init__(self, screen):
        """初始化飞船斌获取其初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放到屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
