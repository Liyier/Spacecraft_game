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
