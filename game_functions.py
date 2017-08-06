"""
存储该游戏项目所需的运行函数
避免游戏入口alien_invasion.py太长，并使逻辑更容易理解
"""

import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ship, settings, screen, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


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


def update_screen(settings, screen, ship, bullets, aliens):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每循环一次重新填充一次屏幕
    screen.fill(settings.bg_color)
    ship.blitme()
    # 估计有self.image继承于Sprite的元素编组能够调用
    aliens.draw(screen)
    # 在飞船和外星人后面重绘所有子弹
    draw_bullets(bullets)
    # 让最近绘制的屏幕可见(绘制一个空屏幕，擦去旧屏幕)
    pygame.display.flip()


def update_bullets(bullets, aliens):
    """更新子弹的位置，并删除已消失的子弹"""
    bullets.update()
    # Bullet继承于Sprite, 估计有update函数, 可以通过编组bullets调用,sprites函数 返回一个列表
    for bullet in bullets.sprites():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查是否有子弹击中了外星人, 有就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


def draw_bullets(bullets):
    """绘制子弹编组"""
    for bullet in bullets:
        bullet.draw_bullet()


def fire_bullet(settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建一颗子弹并加入编组中
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(settings, screen, aliens, ship):
    """创建外星人群"""
    alien = Alien(settings, screen)
    aliens_number = get_aliens_number(settings, alien.rect.width)
    rows_number = get_rows_nunber(settings, ship.rect.height, alien.rect.height)
    for row_number in range(rows_number):
        for alien_number in range(aliens_number):
            create_alien(settings, screen, aliens, alien_number, row_number)


def get_aliens_number(settings, alien_width):
    """计算每行可以容纳多少人"""
    available_space_x = settings.screen_width - 2*alien_width
    aliens_number = int(available_space_x/(2*alien_width))
    return aliens_number


def create_alien(settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并把他放在当前行"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)


def get_rows_nunber(settings, ship_height, alien_height):
    """计算屏幕可以容纳多少行外星人"""
    available_space_y = settings.screen_height - 3*alien_height - ship_height
    rows_number = int(available_space_y/(2*alien_height))
    return rows_number


def update_aliens(settings, aliens):
    """更新飞船位置"""
    check_fleet_edges(settings, aliens)
    aliens.update()


def change_fleet_direction(settings, aliens):
    """将整群外星人下移,并改变他们的方向"""
    for alien in aliens:
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def check_fleet_edges(settings, aliens):
    """有外星人到达边缘就采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break
