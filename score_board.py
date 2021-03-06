import pygame.ftfont
from ship import Ship
from pygame.sprite import Group


class Score(object):
    """显示得分信息的类"""

    def __init__(self, settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # 显示得分信息时的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.ftfont.SysFont(None, 48)

        # 准备初始得分图像
        self.prep_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        """将得分转换成一幅渲染的图像"""
        # 将得分圆整
        rounded_score = round(self.stats.score, -1)  # -1 取10的整数倍
        score_str = '{:,}'.format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # 将屏幕放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom+10

    def prep_ship(self):
        """显示剩下的飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.settings, self.screen)
            ship.rect.x = 10 + ship_number*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制飞船
        self.ships.draw(self.screen)
