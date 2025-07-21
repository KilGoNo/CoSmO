# <------ модули
import pygame
import random
import sys
import time
# <------ сокарщение в коде
watch = pygame.time.Clock()
rect_org = pygame.draw
# <------ работа с дисплейем
pygame.init()
screen = pygame.display.set_mode((700, 1000))
pygame.display.set_caption('Космос')
icon = pygame.image.load('files/icon.png').convert_alpha()
pygame.display.set_icon(icon)
# <------ главное меню с текстом
menu_main_background = pygame.image.load('files/menu_fan.png').convert_alpha()
text_menu_main = pygame.font.Font('files/zubilo-black.otf', 140)
text_menu_main_render = text_menu_main.render('Cosmo', False, (194, 28, 255))
# <------ кнопка с текстом уровни в главном меню
text_menu_main_start = pygame.font.Font('files/Шрифт Майнкрафт.ttf', 70)
text_menu_main_start_render = text_menu_main_start.render('Старт', False, (201, 54, 54))
# <------ задний фон
background = pygame.image.load('files/space-galaxy-background.jpg').convert_alpha()
# <------ стрелка для выхода в меню
text_menu = pygame.font.Font('files/Шрифт Майнкрафт.ttf', 35)
text_restart_menu = text_menu.render('меню', False, (138, 242, 168))
# <------ игрок
player_ran = pygame.image.load('player/player_1.png').convert_alpha()
player_x = 280
player_y = 850
player_speed_level_max = 8
player_speed = 5
player_speed_main = 5
player_speed_stop = 0
# <------ патрон
bullet = pygame.image.load('files/free-icon-bullet-2218066.png').convert_alpha()
bullets = []
bullet_speed = 7
# <------ музыка
bg_music = pygame.mixer.Sound('files/kosmos-28439.mp3')
bg_bullet = pygame.mixer.Sound('files/laser-blast-descend_gy7c5deo.mp3')
bg_loss = pygame.mixer.Sound('files/oglushitelnyiy-blizkiy-vzryiv.mp3')
bg_music.play()
m = 0
mm = 0
# <------ цыфры для уровня
numbers = [
    pygame.image.load('numbers/number_1.png').convert_alpha(),
    pygame.image.load('numbers/number_2.png').convert_alpha(),
    pygame.image.load('numbers/number_3.png').convert_alpha(),
    pygame.image.load('numbers/number_4.png').convert_alpha(),
    pygame.image.load('numbers/number_5.png').convert_alpha(),
    pygame.image.load('numbers/number_6.png').convert_alpha(),
    pygame.image.load('numbers/number_7.png').convert_alpha(),
    pygame.image.load('numbers/number_8.png').convert_alpha(),
    pygame.image.load('numbers/number_9.png').convert_alpha(),
    pygame.image.load('numbers/number_10.png').convert_alpha()
]
left_arrow = pygame.image.load('files/стрелка_влево.png').convert_alpha()
# <------ враг
stone = pygame.image.load('files/stone.png').convert_alpha()
stone_enemy_0 = []
stone_enemy_1 = []
stone_enemy_2 = []
stone_enemy_3 = []
stone_enemy_4 = []
stone_y = -200
stone_speed_stop = 0
stone_speed_level_1 = 1
stone_speed_level_2 = 2
stone_speed_level_3 = 3
stone_speed_level_4 = 4
stone_speed_level_5 = 5 
# <------ взырв врага
boom_stone = pygame.image.load('enemy_explosion/enemy_explosion__0.jpg').convert_alpha()
boom_stone_walk = [
    pygame.image.load('enemy_explosion/enemy_explosion__0.jpg').convert_alpha(),
    pygame.image.load('enemy_explosion/enemy_explosion__1.jpg').convert_alpha(),
    pygame.image.load('enemy_explosion/enemy_explosion__2.jpg').convert_alpha(),
    pygame.image.load('enemy_explosion/enemy_explosion__3.jpg').convert_alpha(),
    pygame.image.load('enemy_explosion/enemy_explosion__4.jpg').convert_alpha(),
    pygame.image.load('enemy_explosion/enemy_explosion__5.jpg').convert_alpha(),
    pygame.image.load('enemy_explosion/enemy_explosion__6.jpg').convert_alpha(),
    pygame.image.load('enemy_explosion/enemy_explosion__7.jpg').convert_alpha(),
    pygame.image.load('enemy_explosion/enemy_explosion__8.jpg').convert_alpha(),
    pygame.image.load('enemy_explosion/enemy_explosion__9.jpg').convert_alpha(),
    pygame.image.load('enemy_explosion/enemy_explosion__10.jpg').convert_alpha(),
    pygame.image.load('enemy_explosion/enemy_explosion__11.jpg').convert_alpha(),
]
boom_stone_count = 0
# <------ взры карабля при смерти
boom_player = pygame.image.load('boom pleyer/explosion_1.png').convert_alpha()
boom_walk = [
    pygame.image.load('boom pleyer/explosion_1.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_2.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_3.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_4.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_5.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_6.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_7.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_8.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_9.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_10.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_11.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_12.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_13.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_14.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_15.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_16.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_17.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_18.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_19.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_20.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_21.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_22.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_23.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_24.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_25.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_26.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_27.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_28.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_29.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_30.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_31.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_32.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_33.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_34.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_35.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_36.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_37.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_38.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_38.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_39.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_40.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_41.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_42.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_43.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_44.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_45.png').convert_alpha(),
    pygame.image.load('boom pleyer/explosion_46.png').convert_alpha(),
]
boom_count = 0
# <------ импорт текстур с меню настроек
setting_stop = pygame.image.load('files/free-icon-pause-11450250 (2).png').convert_alpha()
setting_play = pygame.image.load('files/free-icon-end-9403126.png').convert_alpha()
# <------ импорт текстуры текстов и крестика
level_text_5 = pygame.image.load('files/Надпись для уровня 5.png')
level_text_6 = pygame.image.load('files/Надпись для уровня 6.png')
cross_level_text = pygame.image.load('files/free-icon-cross-mark-4225690.png')
# <------ счет
check = pygame.font.Font(None, 75)
check_text = check.render('счет', False, (134, 94, 242))
# <------ работа с экраном проигрыша
text = pygame.font.Font('files/Шрифт Майнкрафт.ttf', 35)
text_load = text.render('Проигрыш, ваш счёт:', False, (242, 33, 71))
text_restart = text.render('Играть снова', False, (242, 33, 71))
# <------ таймер для врага
stone_timer = pygame.USEREVENT + 1
pygame.time.set_timer(stone_timer, 1000)
# <------ начало цикла
lavel_1 = 0
lavel_2 = 0
lavel_3 = 0
lavel_4 = 0
lavel_5_1 = 0
lavel_5_2 = 0
lavel_6_1 = 0
lavel_6_2 = 0
runnung = True
menu_level = 0
menu_main = 1
# <------ назначение клавиш на клавиатуре изменения кнопок
key_SPACE = pygame.K_SPACE
# <------ счёт очков
chet = 0
chet_max = 100
while runnung:
    # <------ мышка и клавиатура
    mouse = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    # <------ настройка и отрисовка главного менгю игры
    if menu_main == 1:
        screen.blit(menu_main_background, (0, 0))
        screen.blit(text_menu_main_render, (150, 10))
        menu_start_2 = rect_org.rect(screen, (23, 90, 191), pygame.Rect((150, 535), (420, 150)))
        menu_start_1 = rect_org.rect(screen, (91, 151, 240), pygame.Rect((160, 545), (400, 125)))
        screen.blit(text_menu_main_start_render, (190, 550))
        if menu_start_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print('Старт меню уровней')
            menu_main = 0
            menu_level = 1
    # <------ настройка и оторисовка главного меню уровней
    if menu_level == 1:
        screen.fill((39, 214, 182))
        # <------ отсрисовка квадрата вокруг цифр
            # <------первый ряд меню
        numbers_1_rect = numbers[0].get_rect(topleft=(40, 200))
        numbers_2_rect = numbers[1].get_rect(topleft=(210, 200))
        numbers_3_rect = numbers[2].get_rect(topleft=(372, 200))
        numbers_4_rect = numbers[3].get_rect(topleft=(532, 200))
            # <------второй ряд меню
        numbers_5_rect = numbers[4].get_rect(topleft=(210, 375))
        numbers_6_rect = numbers[5].get_rect(topleft=(372, 375))
        # <------ отрисовка текстуры цифр
            # <------первый ряд меню
        screen.blit(numbers[0], (40, 200))
        screen.blit(numbers[1], (210, 200))
        screen.blit(numbers[2], (372, 200))
        screen.blit(numbers[3], (532, 200))
            # <------второй ряд меню
        screen.blit(numbers[4], (210, 375))
        screen.blit(numbers[5], (372, 375))
        # <------ отсрисовка тестуры стрелки и квадртата возле неё
        screen.blit(left_arrow, (290, 700))
        left_arrow_rect = left_arrow.get_rect(topleft=(290, 700))
        if left_arrow_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            menu_level = 0
            menu_main = 1
        # <------ прокерка нажатия мышки на уровень
        if numbers_1_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print('Старт первого уровня')
            player_x = 280
            player_y = 850
            menu_level = 0
            lavel_1 = 1
            stone_enemy_0.clear()
        if numbers_2_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print('Старт второго уровня')
            player_x = 280
            player_y = 850
            menu_level = 0
            lavel_2 = 1
            stone_enemy_0.clear()
            stone_enemy_1.clear()
        if numbers_3_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print('Старт третьего уровня')
            player_x = 280
            player_y = 850
            menu_level = 0
            lavel_3 = 1
            stone_enemy_0.clear()
            stone_enemy_1.clear()
            stone_enemy_2.clear()
            stone_enemy_3.clear()
        if numbers_4_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print('Старт четвёртого уровня')
            player_x = 280
            player_y = 850
            menu_level = 0
            lavel_4 = 1
            stone_enemy_0.clear()
            stone_enemy_1.clear()
            stone_enemy_2.clear()
            stone_enemy_3.clear()
            stone_enemy_4.clear()
        if numbers_5_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print('Старт пятого уровня')
            player_x = 280
            player_y = 850
            menu_level = 0
            lavel_5_1 = 1
            stone_enemy_0.clear()
            stone_enemy_1.clear()
            stone_enemy_2.clear()
            stone_enemy_3.clear()
            stone_enemy_4.clear()
        if numbers_6_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print('Старт шестого уровня')
            player_x = 280
            player_y = 850
            menu_level = 0
            lavel_6_1 = 1
            stone_enemy_0.clear()
            stone_enemy_1.clear()
            stone_enemy_2.clear()
            stone_enemy_3.clear()
            stone_enemy_4.clear()
    # <------ задаем рандомное значение для камня на оси X
    stone_enemy_0_1 = random.randrange(25,600)
    stone_enemy_0_2 = random.randrange(25, 600)
    stone_enemy_0_3 = random.randrange(25,600)
    stone_enemy_0_4 = random.randrange(25,600)
    stone_enemy_0_5 = random.randrange(25,600)
    # <------ отсрисовываем квадрат вокруг камня
    stone_rect_0_1 = stone.get_rect(topleft=(stone_enemy_0_1, stone_y))
    stone_rect_0_2 = stone.get_rect(topleft=(stone_enemy_0_2, stone_y))
    stone_rect_0_3 = stone.get_rect(topleft=(stone_enemy_0_3, stone_y))
    stone_rect_0_4 = stone.get_rect(topleft=(stone_enemy_0_4, stone_y))
    stone_rect_0_5 = stone.get_rect(topleft=(stone_enemy_0_5, stone_y))
    # <------ отсрисовываем квадрат вокруг игрока и патрона
    player_rect = player_ran.get_rect(topleft=(player_x, player_y))
    bullet_rect = bullet.get_rect(topleft=(player_x, player_y))
    # <------ отсрисовываем квадрат вокруг крестика из текста на уровне
    cross_level_text_rect = cross_level_text.get_rect(topleft=(565, 273))
    # <------ отсрисовываем квадрат для меня настроек
    setting_rect_1 = setting_stop.get_rect(topleft=(660, 10))
    setting_rect_2 = setting_play.get_rect(topleft=(662, 50))
    # <------ острисовываем квадрат для текста во время проигрыша
    text_restart_rect = text_restart.get_rect(topleft=(150, 450))
    text_restart_menu_rect = text_restart_menu.get_rect(topleft=(270, 800))
    # <------ работа над первым уровнем
    if lavel_1 == 1:
        #  <------ проверям наведение мышки на квадрат настроек - рабоатет для всех уровней
        if setting_rect_1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bg_music.stop()
            player_speed_main = player_speed_stop
            stone_speed_level_1 = stone_speed_stop
            m = 0
            key_SPACE = 0
            bullet_speed = 0
        if setting_rect_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    if el.y < -50:
                        stone_enemy_0.pop(i)
            key_SPACE = pygame.K_SPACE
            player_speed_main = player_speed
            stone_speed_level_1 = 1
            bullet_speed = 7
            if m == 0:
                bg_music.play(loops=0)
                m = 1

        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))

        text_cheat = text.render(f"{chet}", True, (242, 33, 71))
        text_rect = text_cheat.get_rect(center=(350, 50))
        screen.blit(text_cheat, text_rect)
#  <------ начало всего для уровня
        if stone_enemy_0:
            for (i, el) in enumerate(stone_enemy_0):
                screen.blit(stone, el)
                el.y += stone_speed_level_1

                if el.y > 1500:
                    stone_enemy_0.pop(i)

                if player_rect.colliderect(el):
                    lavel_1 = 2
        if bullets:
            for el in bullets:
                screen.blit(bullet, (el.x, el.y))
                el.y -= bullet_speed

                if el.y < -50:
                    bullets.pop(0)
                if stone_enemy_0:
                    for (index, ghost_el) in enumerate(stone_enemy_0):
                        if el.colliderect(ghost_el):
                            stone_enemy_0.pop(index)
                            chet += 1
                            # screen.blit(boom_stone_walk[boom_stone_count], (500, 250))
                            # if boom_stone_count == 8:
                            #     pass
                            # else:
                            #     boom_stone_count += 1
    if lavel_1 == 2:
        bg_music.stop()
        stone_enemy_0.clear()
        bullets.clear()
        player_speed_main = player_speed_stop
        key = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(boom_walk[boom_count], (player_x - 90, player_y - 75))
        if boom_count == 46:
            pass
        else:
            boom_count += 1
        if mm == 0:
            bg_loss.play(loops=0)
            mm = 1
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((120, 418), (460, 110)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((130, 429), (440, 90)))
        screen.blit(text_load, (50, 180))
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((240, 795), (220, 75)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((245, 800), (210, 65)))
        screen.blit(text_restart_menu, (270, 800))
        text_cheat = text.render(f"{chet}", False, (242, 33, 71))
        text_rect_2 = text_cheat.get_rect(center=(350, 290))
        screen.blit(text_cheat, text_rect_2)
        screen.blit(text_restart, text_restart_rect)

        if text_restart_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            lavel_1 = 0
            lavel_2 = 0
            lavel_3 = 0
            lavel_4 = 0
            lavel_5_1 = 0
            lavel_5_2 = 0
            lavel_6_1 = 0
            lavel_6_2 = 0
            menu_level = 0
            menu_main = 1
            player_speed_main = player_speed
            boom_count = 0
            bg_music.play(loops=0)
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE
        if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            player_x = 280
            player_y = 850
            lavel_1 = 1
            bg_music.play()
            boom_count = 0
            player_speed_main = player_speed
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE

        # <------ работа над вторым уровнем
    # <------ работа над вторым уровнем
    if lavel_2 == 1:
        #  <------ проверям наведение мышки на квадрат настроек - рабоатет для всех уровней
        if setting_rect_1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bg_music.stop()
            player_speed_main = player_speed_stop
            stone_speed_level_2 = stone_speed_stop
            m = 0
            key_SPACE = 0
            bullet_speed = 0
        if setting_rect_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    if el.y < -50:
                        stone_enemy_0.pop(i)
            key_SPACE = pygame.K_SPACE
            player_speed_main = player_speed
            stone_speed_level_2 = 2
            bullet_speed = 7
            if m == 0:
                bg_music.play(loops=0)
                m = 1

        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))

        text_cheat = text.render(f"{chet}", True, (242, 33, 71))
        text_rect = text_cheat.get_rect(center=(350, 50))
        screen.blit(text_cheat, text_rect)
        #  <------ начало всего для уровня
        if stone_enemy_0:
            for (i, el) in enumerate(stone_enemy_0):
                screen.blit(stone, el)
                el.y += stone_speed_level_2

                if el.y > 1500:
                    stone_enemy_0.pop(i)

                if player_rect.colliderect(el):
                    lavel_2 = 2
        if stone_enemy_1:
            for (i, el) in enumerate(stone_enemy_1):
                screen.blit(stone, el)
                el.y += stone_speed_level_2

                if el.y > 1500:
                    stone_enemy_1.pop(i)

                if player_rect.colliderect(el):
                    lavel_2 = 2
        if bullets:
            for el in bullets:
                screen.blit(bullet, (el.x, el.y))
                el.y -= bullet_speed

                if el.y < -50:
                    bullets.pop(0)

                if stone_enemy_0:
                    for (index, ghost_el) in enumerate(stone_enemy_0):
                        if el.colliderect(ghost_el):
                            stone_enemy_0.pop(index)
                            chet += 1
    if lavel_2 == 2:
        bg_music.stop()
        stone_enemy_0.clear()
        stone_enemy_1.clear()
        bullets.clear()
        player_speed_main = player_speed_stop
        key = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(boom_walk[boom_count], (player_x - 90, player_y - 75))
        if boom_count == 46:
            pass
        else:
            boom_count += 1
        if mm == 0:
            bg_loss.play(loops=0)
            mm = 1
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((120, 418), (460, 110)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((130, 429), (440, 90)))
        screen.blit(text_load, (50, 180))
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((240, 795), (220, 75)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((245, 800), (210, 65)))
        screen.blit(text_restart_menu, (270, 800))
        text_cheat = text.render(f"{chet}", False, (242, 33, 71))
        text_rect_2 = text_cheat.get_rect(center=(350, 290))
        screen.blit(text_cheat, text_rect_2)
        screen.blit(text_restart, text_restart_rect)

        if text_restart_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            lavel_1 = 0
            lavel_2 = 0
            lavel_3 = 0
            lavel_4 = 0
            lavel_5_1 = 0
            lavel_5_2 = 0
            lavel_6_1 = 0
            lavel_6_2 = 0
            menu_level = 0
            menu_main = 1
            player_speed_main = player_speed
            boom_count = 0
            bg_music.play(loops=0)
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE
        if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            player_x = 280
            player_y = 850
            lavel_2 = 1
            bg_music.play()
            boom_count = 0
            player_speed_main = player_speed
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE
        # <------ работа над третьим уровнем
    # <------ работа над третьим уровнем
    if lavel_3 == 1:
        if setting_rect_1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bg_music.stop()
            player_speed_main = player_speed_stop
            stone_speed_level_3 = stone_speed_stop
            m = 0
            key_SPACE = 0
            bullet_speed = 0
        if setting_rect_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    if el.y < -50:
                        stone_enemy_0.pop(i)
            key_SPACE = pygame.K_SPACE
            player_speed_main = player_speed
            stone_speed_level_3 = 3
            bullet_speed = 7
            if m == 0:
                bg_music.play(loops=0)
                m = 1

        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))

        text_cheat = text.render(f"{chet}", True, (242, 33, 71))
        text_rect = text_cheat.get_rect(center=(350, 50))
        screen.blit(text_cheat, text_rect)
        #  <------ начало всего для уровня
        if stone_enemy_0:
            for (i, el) in enumerate(stone_enemy_0):
                screen.blit(stone, el)
                el.y += stone_speed_level_3

                if el.y > 1500:
                    stone_enemy_0.pop(i)

                if player_rect.colliderect(el):
                    lavel_3 = 2
        if stone_enemy_1:
            for (i, el) in enumerate(stone_enemy_1):
                screen.blit(stone, el)
                el.y += stone_speed_level_3

                if el.y > 1500:
                    stone_enemy_1.pop(i)

                if player_rect.colliderect(el):
                    lavel_3 = 2
        if stone_enemy_2:
            for (i, el) in enumerate(stone_enemy_2):
                screen.blit(stone, el)
                el.y += stone_speed_level_3

                if el.y > 1500:
                    stone_enemy_2.pop(i)

                if player_rect.colliderect(el):
                    lavel_3 = 2
        if bullets:
            for el in bullets:
                screen.blit(bullet, (el.x, el.y))
                el.y -= bullet_speed

                if el.y < -50:
                    bullets.pop(0)

                if stone_enemy_0:
                    for (index, ghost_el) in enumerate(stone_enemy_0):
                        if el.colliderect(ghost_el):
                            stone_enemy_0.pop(index)
                            chet += 1
                if stone_enemy_1:
                    for (index, ghost_el) in enumerate(stone_enemy_1):
                        if el.colliderect(ghost_el):
                            stone_enemy_1.pop(index)
                            chet += 1
                if stone_enemy_2:
                    for (index, ghost_el) in enumerate(stone_enemy_2):
                        if el.colliderect(ghost_el):
                            stone_enemy_2.pop(index)
                            chet += 1
    if lavel_3 == 2:
        bg_music.stop()
        stone_enemy_0.clear()
        stone_enemy_1.clear()
        stone_enemy_2.clear()
        bullets.clear()
        player_speed_main = player_speed_stop
        key_SPACE = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(boom_walk[boom_count], (player_x - 90, player_y - 75))
        if boom_count == 46:
            pass
        else:
            boom_count += 1
        if mm == 0:
            bg_loss.play(loops=0)
            mm = 1
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((120, 418), (460, 110)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((130, 429), (440, 90)))
        screen.blit(text_load, (50, 180))
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((240, 795), (220, 75)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((245, 800), (210, 65)))
        screen.blit(text_restart_menu, (270, 800))
        text_cheat = text.render(f"{chet}", False, (242, 33, 71))
        text_rect_2 = text_cheat.get_rect(center=(350, 290))
        screen.blit(text_cheat, text_rect_2)
        screen.blit(text_restart, text_restart_rect)

        if text_restart_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            lavel_1 = 0
            lavel_2 = 0
            lavel_3 = 0
            lavel_4 = 0
            lavel_5_1 = 0
            lavel_5_2 = 0
            lavel_6_1 = 0
            lavel_6_2 = 0
            menu_level = 0
            menu_main = 1
            player_speed_main = player_speed
            bg_music.play(loops=0)
            m = 0
            mm = 0
            chet = 0
            boom_count = 0
            key_SPACE = pygame.K_SPACE
        if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            player_x = 280
            player_y = 850
            lavel_3 = 1
            bg_music.play()
            boom_count = 0
            player_speed_main = player_speed
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE
    # <------ работа над четвертым уровнем
    if lavel_4 == 1:
        if setting_rect_1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bg_music.stop()
            player_speed_main = player_speed_stop
            stone_speed_level_4 = stone_speed_stop
            m = 0
            key_SPACE = 0
            bullet_speed = 0
        if setting_rect_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_4

                    if el.y > 1500:
                        stone_enemy_0.pop(i)

                    if player_rect.colliderect(el):
                        lavel_4 = 2
            if stone_enemy_1:
                for (i, el) in enumerate(stone_enemy_1):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_4

                    if el.y > 1500:
                        stone_enemy_1.pop(i)

                    if player_rect.colliderect(el):
                        lavel_4 = 2
            if stone_enemy_2:
                for (i, el) in enumerate(stone_enemy_2):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_4

                    if el.y > 1500:
                        stone_enemy_2.pop(i)

                    if player_rect.colliderect(el):
                        lavel_4 = 2
            if stone_enemy_3:
                for (i, el) in enumerate(stone_enemy_3):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_4

                    if el.y > 1500:
                        stone_enemy_3.pop(i)

                    if player_rect.colliderect(el):
                        lavel_4 = 2
            key_SPACE = pygame.K_SPACE
            player_speed_main = player_speed
            stone_speed_level_4 = 4
            bullet_speed = 7
            if m == 0:
                bg_music.play(loops=0)
                m = 1

        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))

        text_cheat = text.render(f"{chet}", True, (242, 33, 71))
        text_rect = text_cheat.get_rect(center=(350, 50))
        screen.blit(text_cheat, text_rect)
        #  <------ начало всего для уровня
        if stone_enemy_0:
            for (i, el) in enumerate(stone_enemy_0):
                screen.blit(stone, el)
                el.y += stone_speed_level_4

                if el.y > 1500:
                    stone_enemy_0.pop(i)

                if player_rect.colliderect(el):
                    lavel_4 = 2
        if stone_enemy_1:
            for (i, el) in enumerate(stone_enemy_1):
                screen.blit(stone, el)
                el.y += stone_speed_level_4

                if el.y > 1500:
                    stone_enemy_1.pop(i)

                if player_rect.colliderect(el):
                    lavel_4 = 2
        if stone_enemy_2:
            for (i, el) in enumerate(stone_enemy_2):
                screen.blit(stone, el)
                el.y += stone_speed_level_4

                if el.y > 1500:
                    stone_enemy_2.pop(i)

                if player_rect.colliderect(el):
                    lavel_4 = 2
        if stone_enemy_3:
            for (i, el) in enumerate(stone_enemy_3):
                screen.blit(stone, el)
                el.y += stone_speed_level_4

                if el.y > 1500:
                    stone_enemy_3.pop(i)

                if player_rect.colliderect(el):
                    lavel_4 = 2
        if bullets:
            for el in bullets:
                screen.blit(bullet, (el.x, el.y))
                el.y -= bullet_speed

                if el.y < -50:
                    bullets.pop(0)

                if stone_enemy_0:
                    for (index, ghost_el) in enumerate(stone_enemy_0):
                        if el.colliderect(ghost_el):
                            stone_enemy_0.pop(index)
                            chet += 1
                if stone_enemy_1:
                    for (index, ghost_el) in enumerate(stone_enemy_1):
                        if el.colliderect(ghost_el):
                            stone_enemy_1.pop(index)
                            chet += 1
                if stone_enemy_2:
                    for (index, ghost_el) in enumerate(stone_enemy_2):
                        if el.colliderect(ghost_el):
                            stone_enemy_2.pop(index)
                            chet += 1
                if stone_enemy_3:
                    for (index, ghost_el) in enumerate(stone_enemy_3):
                        if el.colliderect(ghost_el):
                            stone_enemy_3.pop(index)
                            chet += 1
    if lavel_4 == 2:
        bg_music.stop()
        stone_enemy_0.clear()
        stone_enemy_1.clear()
        stone_enemy_2.clear()
        stone_enemy_3.clear()
        bullets.clear()
        player_speed_main = player_speed_stop
        key_SPACE = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(boom_walk[boom_count], (player_x - 90, player_y - 75))
        if boom_count == 46:
            pass
        else:
            boom_count += 1
        if mm == 0:
            bg_loss.play(loops=0)
            mm = 1
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((120, 418), (460, 110)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((130, 429), (440, 90)))
        screen.blit(text_load, (50, 180))
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((240, 795), (220, 75)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((245, 800), (210, 65)))
        screen.blit(text_restart_menu, (270, 800))
        text_cheat = text.render(f"{chet}", False, (242, 33, 71))
        text_rect_2 = text_cheat.get_rect(center=(350, 290))
        screen.blit(text_cheat, text_rect_2)
        screen.blit(text_restart, text_restart_rect)

        if text_restart_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            lavel_1 = 0
            lavel_2 = 0
            lavel_3 = 0
            lavel_4 = 0
            lavel_5_1 = 0
            lavel_5_2 = 0
            lavel_6_1 = 0
            lavel_6_2 = 0
            menu_level = 0
            menu_main = 1
            player_speed_main = player_speed
            bg_music.play(loops=0)
            m = 0
            mm = 0
            chet = 0
            boom_count = 0
            key_SPACE = pygame.K_SPACE
        if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            player_x = 280
            player_y = 850
            lavel_4 = 1
            bg_music.play()
            boom_count = 0
            player_speed_main = player_speed
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE
    # <------ работа над пятым уровнем
    if lavel_5_1 == 1:
        player_speed_main = player_speed_stop
        stone_speed_level_5 = stone_speed_stop
        m = 0
        key_SPACE = 0
        bullet_speed = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))
        screen.blit(level_text_5, (100, 270))
        screen.blit(cross_level_text, (565, 273))
        if cross_level_text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    if el.y > 1500:
                        stone_enemy_0.pop(i)
            if stone_enemy_1:
                for (i, el) in enumerate(stone_enemy_1):
                    if el.y > 1500:
                        stone_enemy_1.pop(i)
            if stone_enemy_2:
                for (i, el) in enumerate(stone_enemy_2):
                    if el.y > 1500:
                        stone_enemy_2.pop(i)
            if stone_enemy_2:
                for (i, el) in enumerate(stone_enemy_2):
                    if el.y > 1500:
                        stone_enemy_0.pop(i)
            if stone_enemy_3:
                for (i, el) in enumerate(stone_enemy_3):
                    if el.y > 1500:
                        stone_enemy_3.pop(i)
            if stone_enemy_4:
                for (i, el) in enumerate(stone_enemy_4):
                    if el.y > 1500:
                        stone_enemy_4.pop(i)
            key_SPACE = pygame.K_SPACE
            player_speed_main = player_speed
            stone_speed_level_5 = 7
            bullet_speed = 7
            lavel_5_2 = 1
            lavel_5_1 = 0
    if lavel_5_2 == 1:
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))
        watch.tick(60)
        if setting_rect_1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bg_music.stop()
            player_speed_main = player_speed_stop
            stone_speed_level_5 = stone_speed_stop
            m = 0
            key_SPACE = 0
            bullet_speed = 0
        if setting_rect_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_5

                    if el.y > 1500:
                        stone_enemy_0.pop(i)

            if stone_enemy_1:
                for (i, el) in enumerate(stone_enemy_1):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_5

                    if el.y > 1500:
                        stone_enemy_1.pop(i)

            if stone_enemy_2:
                for (i, el) in enumerate(stone_enemy_2):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_5

                    if el.y > 1500:
                        stone_enemy_2.pop(i)

            if stone_enemy_3:
                for (i, el) in enumerate(stone_enemy_3):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_5

                    if el.y > 1500:
                        stone_enemy_3.pop(i)
            if stone_enemy_4:
                for (i, el) in enumerate(stone_enemy_4):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_5

                    if el.y > 1500:
                        stone_enemy_4.pop(i)
        if m == 0:
            bg_music.play(loops=0)
            m = 1
        text_cheat = text.render(f"{chet}", True, (242, 33, 71))
        text_rect = text_cheat.get_rect(center=(350, 50))
        screen.blit(text_cheat, text_rect)
        #  <------ начало всего для уровня
        if stone_enemy_0:
            for (i, el) in enumerate(stone_enemy_0):
                screen.blit(stone, el)
                el.y += stone_speed_level_5

                if el.y > 1500:
                    stone_enemy_0.pop(i)

                if player_rect.colliderect(el):
                    lavel_5_2 = 2
        if stone_enemy_1:
            for (i, el) in enumerate(stone_enemy_1):
                screen.blit(stone, el)
                el.y += stone_speed_level_5

                if el.y > 1500:
                    stone_enemy_1.pop(i)

                if player_rect.colliderect(el):
                    lavel_5_2 = 2
        if stone_enemy_2:
            for (i, el) in enumerate(stone_enemy_2):
                screen.blit(stone, el)
                el.y += stone_speed_level_5

                if el.y > 1500:
                    stone_enemy_2.pop(i)

                if player_rect.colliderect(el):
                    lavel_5_2 = 2
        if stone_enemy_3:
            for (i, el) in enumerate(stone_enemy_3):
                screen.blit(stone, el)
                el.y += stone_speed_level_5

                if el.y > 1500:
                    stone_enemy_3.pop(i)

                if player_rect.colliderect(el):
                    lavel_5_2 = 2
        if stone_enemy_4:
            for (i, el) in enumerate(stone_enemy_4):
                screen.blit(stone, el)
                el.y += stone_speed_level_5

                if el.y > 1500:
                    stone_enemy_4.pop(i)

                if player_rect.colliderect(el):
                    lavel_5_2 = 2
        if bullets:
            for el in bullets:
                screen.blit(bullet, (el.x, el.y))
                el.y -= bullet_speed

                if el.y < -50:
                    bullets.pop(0)

                if stone_enemy_0:
                    for (index, ghost_el) in enumerate(stone_enemy_0):
                        if el.colliderect(ghost_el):
                            stone_enemy_0.pop(index)
                            chet += 1
                if stone_enemy_1:
                    for (index, ghost_el) in enumerate(stone_enemy_1):
                        if el.colliderect(ghost_el):
                            stone_enemy_1.pop(index)
                            chet += 1
                if stone_enemy_2:
                    for (index, ghost_el) in enumerate(stone_enemy_2):
                        if el.colliderect(ghost_el):
                            stone_enemy_2.pop(index)
                            chet += 1
                if stone_enemy_3:
                    for (index, ghost_el) in enumerate(stone_enemy_3):
                        if el.colliderect(ghost_el):
                            stone_enemy_3.pop(index)
                            chet += 1
                if stone_enemy_4:
                    for (index, ghost_el) in enumerate(stone_enemy_4):
                        if el.colliderect(ghost_el):
                            stone_enemy_4.pop(index)
                            chet += 1
    if lavel_5_2 == 2:
        bg_music.stop()
        stone_enemy_0.clear()
        stone_enemy_1.clear()
        stone_enemy_2.clear()
        stone_enemy_3.clear()
        stone_enemy_4.clear()
        bullets.clear()
        player_speed_main = player_speed_stop
        key_SPACE = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(boom_walk[boom_count], (player_x - 90, player_y - 75))
        if boom_count == 46:
            pass
        else:
            boom_count += 1
        if mm == 0:
            bg_loss.play(loops=0)
            mm = 1
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((120, 418), (460, 110)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((130, 429), (440, 90)))
        screen.blit(text_load, (50, 180))
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((240, 795), (220, 75)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((245, 800), (210, 65)))
        screen.blit(text_restart_menu, (270, 800))
        text_cheat = text.render(f"{chet}", False, (242, 33, 71))
        text_rect_2 = text_cheat.get_rect(center=(350, 290))
        screen.blit(text_cheat, text_rect_2)
        screen.blit(text_restart, text_restart_rect)

        if text_restart_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            lavel_1 = 0
            lavel_2 = 0
            lavel_3 = 0
            lavel_4 = 0
            lavel_5_1 = 0
            lavel_5_2 = 0
            lavel_6_1 = 0
            lavel_6_2 = 0
            menu_level = 0
            menu_main = 1
            player_speed_main = player_speed
            bg_music.play(loops=0)
            m = 0
            mm = 0
            chet = 0
            boom_count = 0
            key_SPACE = pygame.K_SPACE
        if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            player_x = 280
            player_y = 850
            lavel_5_2 = 1
            bg_music.play()
            boom_count = 0
            player_speed_main = player_speed
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE
    # <------ работа над шестым уровнем
    if lavel_6_1 == 1:
        player_speed_main = player_speed_stop
        stone_speed_level_6 = stone_speed_stop
        m = 0
        key_SPACE = 0
        bullet_speed = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))
        screen.blit(level_text_6, (100, 270))
        screen.blit(cross_level_text, (565, 273))
        if cross_level_text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    if el.y > 1500:
                        stone_enemy_0.pop(i)
            if stone_enemy_1:
                for (i, el) in enumerate(stone_enemy_1):
                    if el.y > 1500:
                        stone_enemy_1.pop(i)
            if stone_enemy_2:
                for (i, el) in enumerate(stone_enemy_2):
                    if el.y > 1500:
                        stone_enemy_2.pop(i)
            if stone_enemy_2:
                for (i, el) in enumerate(stone_enemy_2):
                    if el.y > 1500:
                        stone_enemy_0.pop(i)
            if stone_enemy_3:
                for (i, el) in enumerate(stone_enemy_3):
                    if el.y > 1500:
                        stone_enemy_3.pop(i)
            if stone_enemy_4:
                for (i, el) in enumerate(stone_enemy_4):
                    if el.y > 1500:
                        stone_enemy_4.pop(i)
            key_SPACE = pygame.K_SPACE
            player_speed_main = player_speed
            stone_speed_level_6 = 7
            bullet_speed = 7
            lavel_6_2 = 1
            lavel_6_1 = 0
    if lavel_6_2 == 1:
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))
        watch.tick(45)
        if setting_rect_1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bg_music.stop()
            player_speed_main = player_speed_stop
            stone_speed_level_5 = stone_speed_stop
            m = 0
            key_SPACE = 0
            bullet_speed = 0
        if setting_rect_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_6

                    if el.y > 1500:
                        stone_enemy_0.pop(i)

            if stone_enemy_1:
                for (i, el) in enumerate(stone_enemy_1):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_6

                    if el.y > 1500:
                        stone_enemy_1.pop(i)

            if stone_enemy_2:
                for (i, el) in enumerate(stone_enemy_2):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_6

                    if el.y > 1500:
                        stone_enemy_2.pop(i)

            if stone_enemy_3:
                for (i, el) in enumerate(stone_enemy_3):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_6

                    if el.y > 1500:
                        stone_enemy_3.pop(i)
            if stone_enemy_4:
                for (i, el) in enumerate(stone_enemy_4):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_6

                    if el.y > 1500:
                        stone_enemy_4.pop(i)
        if m == 0:
            bg_music.play(loops=0)
            m = 1
        text_cheat = text.render(f"{chet}", True, (242, 33, 71))
        text_rect = text_cheat.get_rect(center=(350, 50))
        screen.blit(text_cheat, text_rect)
        #  <------ начало всего для уровня
        if stone_enemy_0:
            for (i, el) in enumerate(stone_enemy_0):
                screen.blit(stone, el)
                el.y += stone_speed_level_6

                if el.y > 1500:
                    stone_enemy_0.pop(i)

                if player_rect.colliderect(el):
                    lavel_6_2 = 2
        if stone_enemy_1:
            for (i, el) in enumerate(stone_enemy_1):
                screen.blit(stone, el)
                el.y += stone_speed_level_6

                if el.y > 1500:
                    stone_enemy_1.pop(i)

                if player_rect.colliderect(el):
                    lavel_6_2 = 2
        if stone_enemy_2:
            for (i, el) in enumerate(stone_enemy_2):
                screen.blit(stone, el)
                el.y += stone_speed_level_6

                if el.y > 1500:
                    stone_enemy_2.pop(i)

                if player_rect.colliderect(el):
                    lavel_6_2 = 2
        if stone_enemy_3:
            for (i, el) in enumerate(stone_enemy_3):
                screen.blit(stone, el)
                el.y += stone_speed_level_6

                if el.y > 1500:
                    stone_enemy_3.pop(i)

                if player_rect.colliderect(el):
                    lavel_6_2 = 2
        if stone_enemy_4:
            for (i, el) in enumerate(stone_enemy_4):
                screen.blit(stone, el)
                el.y += stone_speed_level_6

                if el.y > 1500:
                    stone_enemy_4.pop(i)

                if player_rect.colliderect(el):
                    lavel_6_2 = 2
        if bullets:
            for el in bullets:
                screen.blit(bullet, (el.x, el.y))
                el.y -= bullet_speed

                if el.y < -50:
                    bullets.pop(0)

                if stone_enemy_0:
                    for (index, ghost_el) in enumerate(stone_enemy_0):
                        if el.colliderect(ghost_el):
                            stone_enemy_0.pop(index)
                            chet += 1
                if stone_enemy_1:
                    for (index, ghost_el) in enumerate(stone_enemy_1):
                        if el.colliderect(ghost_el):
                            stone_enemy_1.pop(index)
                            chet += 1
                if stone_enemy_2:
                    for (index, ghost_el) in enumerate(stone_enemy_2):
                        if el.colliderect(ghost_el):
                            stone_enemy_2.pop(index)
                            chet += 1
                if stone_enemy_3:
                    for (index, ghost_el) in enumerate(stone_enemy_3):
                        if el.colliderect(ghost_el):
                            stone_enemy_3.pop(index)
                            chet += 1
                if stone_enemy_4:
                    for (index, ghost_el) in enumerate(stone_enemy_4):
                        if el.colliderect(ghost_el):
                            stone_enemy_4.pop(index)
                            chet += 1
    if lavel_6_2 == 2:
        bg_music.stop()
        stone_enemy_0.clear()
        stone_enemy_1.clear()
        stone_enemy_2.clear()
        stone_enemy_3.clear()
        stone_enemy_4.clear()
        bullets.clear()
        player_speed_main = player_speed_stop
        key_SPACE = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(boom_walk[boom_count], (player_x - 90, player_y - 75))
        if boom_count == 46:
            pass
        else:
            boom_count += 1
        if mm == 0:
            bg_loss.play(loops=0)
            mm = 1
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((120, 418), (460, 110)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((130, 429), (440, 90)))
        screen.blit(text_load, (50, 180))
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((240, 795), (220, 75)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((245, 800), (210, 65)))
        screen.blit(text_restart_menu, (270, 800))
        text_cheat = text.render(f"{chet}", False, (242, 33, 71))
        text_rect_2 = text_cheat.get_rect(center=(350, 290))
        screen.blit(text_cheat, text_rect_2)
        screen.blit(text_restart, text_restart_rect)

        if text_restart_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            lavel_1 = 0
            lavel_2 = 0
            lavel_3 = 0
            lavel_4 = 0
            lavel_5_1 = 0
            lavel_5_2 = 0
            lavel_6_1 = 0
            lavel_6_2 = 0
            menu_level = 0
            menu_main = 1
            player_speed_main = player_speed
            bg_music.play(loops=0)
            m = 0
            mm = 0
            chet = 0
            boom_count = 0
            key_SPACE = pygame.K_SPACE
        if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            player_x = 280
            player_y = 850
            lavel_6_2 = 1
            bg_music.play()
            boom_count = 0
            player_speed_main = player_speed
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE
    # <------ пермещение вправо и влево
    if keys[pygame.K_LEFT] and player_x > 25:
        player_x -= player_speed_main
    elif keys[pygame.K_RIGHT] and player_x < 600:
        player_x += player_speed_main
    elif keys[pygame.K_a] and player_x > 25:
        player_x -= player_speed_main
    elif keys[pygame.K_d] and player_x < 600:
        player_x += player_speed_main
    # <------ перемещенение вверх и вниз; ограничеие по перемещению
    if keys[pygame.K_UP]  and player_y > 30:
        player_y -= player_speed_main
    elif keys[pygame.K_DOWN] and player_y < 860:
        player_y += player_speed_main
    elif keys[pygame.K_w] and player_y > 30:
        player_y -= player_speed_main
    elif keys[pygame.K_s] and player_y < 860:
        player_y += player_speed_main
# <------ цикл для кнопок
    for event in pygame.event.get():
        if event. type == pygame.QUIT:
            sys.exit(0)
        if event.type == stone_timer:
            stone_enemy_0.append(stone.get_rect(topleft=(stone_enemy_0_1, stone_y)))
            stone_enemy_0.append(stone.get_rect(topleft=(stone_enemy_0_1, stone_y)))
            stone_enemy_1.append(stone.get_rect(topleft=(stone_enemy_0_2, stone_y)))
            stone_enemy_1.append(stone.get_rect(topleft=(stone_enemy_0_2, stone_y)))
            stone_enemy_2.append(stone.get_rect(topleft=(stone_enemy_0_3, stone_y)))
            stone_enemy_2.append(stone.get_rect(topleft=(stone_enemy_0_3, stone_y)))
            stone_enemy_3.append(stone.get_rect(topleft=(stone_enemy_0_4, stone_y)))
            stone_enemy_3.append(stone.get_rect(topleft=(stone_enemy_0_4, stone_y)))
            stone_enemy_4.append(stone.get_rect(topleft=(stone_enemy_0_5, stone_y)))
            stone_enemy_4.append(stone.get_rect(topleft=(stone_enemy_0_5, stone_y)))
        if (lavel_1 or lavel_2 or lavel_3 or lavel_4 or lavel_5_2 or lavel_6_2) and event.type == pygame.KEYUP and event.key == key_SPACE:
            bullets.append(bullet.get_rect(topleft=(player_x, player_y - 30)))
            bg_bullet.play()
    pygame.display.update()
    watch.tick(120)
