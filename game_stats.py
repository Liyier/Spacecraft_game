"""
跟踪游戏统计信息
"""


class GameStats(object):

    def __init__(self, settings):
        """初始化统计信息"""
        self.settings = settings
        # 游戏启动时处于活跃状态
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit