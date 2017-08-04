"""
存储该游戏项目所需的运行函数
避免游戏入口alien_invasion.py太长，并使逻辑更容易理解
"""

import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ship, settings, screen, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """响应松开"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship, settings, bullets, screen):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每循环一次重新填充一次屏幕
    screen.fill(settings.bg_color)

    ship.update()
    ship.blitme()
    # 在飞船和外星人后面重绘所有子弹
    update_bullets(bullets)
    # 让最近绘制的屏幕可见(绘制一个空屏幕，擦去旧屏幕)
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    bullets.update()
    # Bullet继承于Sprite, 估计有update函数, 可以通过编组bullets调用,sprites函数 返回一个列表
    for bullet in bullets.sprites():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        else:
            bullet.draw_bullet()


def fire_bullet(settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建一颗子弹并加入编组中
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)