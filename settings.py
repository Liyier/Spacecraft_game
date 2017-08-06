"""
存储该游戏所有设置的类
"""


class Settings(object):

    def __init__(self):

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 设置背景色 (r, g, b)-- 0~255(黑~白)

        # 飞船设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # 外星人设置
        self.alien_speed_factor = 1
        # 整群外星人direction 1为向右,-1为向左
        self.fleet_direction = 1
        # 下降速度
        self.fleet_drop_speed = 10
