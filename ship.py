"""
该项目游戏中的ship
将imgae的rect放置在整个游戏屏幕的screen的rect中
pygame 处理rect(矩形)一样处理游戏元素
rect对象有center(估计是元组),centerx,centery等属性
"""
import pygame


class Ship(object):

    def __init__(self, settings, screen):
        """
        初始化飞船斌获取其初始位置
        通过形参settings获取一些飞船设置
        """
        self.screen = screen
        self.settings = settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 移动标志
        self.moving_right = False
        self.moving_left = False

        # 将每艘飞船放到屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性center中存储小数值(即先将rect.centerx转化成浮点数变化位置,再转化回来整数)
        self.center = float(self.rect.centerx)

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.settings.ship_speed_factor

        # 根据self.center(浮点数)更新rect(rect的centerx只接受整数)对象
        self.rect.centerx = self.center
