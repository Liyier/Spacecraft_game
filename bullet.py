"""
Bullet: 子弹类
继承于Sprite
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """飞船发射的子弹"""

    def __init__(self, settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0, 0)处创建一个表示子弹的矩形,在设置其正确的位置
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小鼠表示的子弹位置
        self.y = float(self.rect.y)  # center是指中心, 写x,y 则指坐标点，一般是左上点

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数点-->左上角是(0,0)
        self.y -= self.speed_factor
        # 更新表示子弹rect的位置i
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
