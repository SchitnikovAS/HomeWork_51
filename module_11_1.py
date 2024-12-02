import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000, 626))  # flags = pygame.NOFRAME
pygame.display.set_caption('Margarita')

icon = pygame.image.load('Margaret_ICO.jpg').convert_alpha()
pygame.display.set_icon(icon)
bg = pygame.image.load('background.jpg').convert_alpha()
player = pygame.image.load('margo_right_1.png').convert_alpha()
walk_right = [
    pygame.image.load('margo_right_1.png').convert_alpha(),
    pygame.image.load('margo_right_2.png').convert_alpha(),
    pygame.image.load('margo_right_3.png').convert_alpha(),
    pygame.image.load('margo_right_4.png').convert_alpha(),
]
walk_left = [
    pygame.image.load('margo_left_1.png').convert_alpha(),
    pygame.image.load('margo_left_2.png').convert_alpha(),
    pygame.image.load('margo_left_3.png').convert_alpha(),
    pygame.image.load('margo_left_4.png').convert_alpha()
]
enemy_left = [
    pygame.image.load('flowers_left_1.png').convert_alpha(),
    pygame.image.load('flowers_left_2.png').convert_alpha(),
    pygame.image.load('flowers_left_3.png').convert_alpha(),
    pygame.image.load('flowers_left_4.png').convert_alpha()
]
wolf_left = [
    pygame.image.load('wolf_left_1.png').convert_alpha(),
    pygame.image.load('wolf_left_2.png').convert_alpha(),
    pygame.image.load('wolf_left_3.png').convert_alpha(),
    pygame.image.load('wolf_left_4.png').convert_alpha()
]
bird_left = [
    pygame.image.load('bird_left_1.png').convert_alpha(),
    pygame.image.load('bird_left_2.png').convert_alpha(),
    pygame.image.load('bird_left_3.png').convert_alpha(),
    pygame.image.load('bird_left_4.png').convert_alpha()
]

flower_list_in_game = []
wolf_list_in_game = []
bird_list_in_game = []

lable = pygame.font.Font('LibreFranklin-ExtraLight.ttf', 40)  # задаем шрифт и его размер
lose_lable = lable.render('Game over', True, 'Blue')
restart_lable = lable.render('Restart', True, 'Green')
restart_lable_rect = restart_lable.get_rect(topleft=(400, 350))

bullet = pygame.image.load('bullet_1 100x40.png').convert_alpha()
bullets = []

player_anim_count = 0
bg_x = 0
bg_sound = pygame.mixer.Sound('Maggi_song.mp3')
bg_sound.play()

flower_timer = pygame.USEREVENT + 1
pygame.time.set_timer(flower_timer, 2350)

wolf_timer = pygame.USEREVENT + 3
pygame.time.set_timer(wolf_timer, 5555)

bird_timer = pygame.USEREVENT + 5
pygame.time.set_timer(bird_timer, 10000)

player_speed = 10
player_x = 300
player_y = 425

is_jump = False
jump_count = 10

bullet_left = 5
ICO_ballet = pygame.image.load('lable_bullet.png').convert_alpha()
score = 0

gameplay = True

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1000, 0))

    bullet_lable = lable.render(str(bullet_left), True, 'White')
    screen.blit(bullet_lable, (150, 80))
    screen.blit(ICO_ballet, (30, 70))
    score_lable = lable.render(f'SCORE: {str(score)}', True, 'White')
    screen.blit(score_lable, (30, 120))
    if gameplay:

        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

        if flower_list_in_game:
            for i, el in enumerate(flower_list_in_game):
                screen.blit(enemy_left[player_anim_count], el)
                el.x -= 10
                if el.x < -10:
                    flower_list_in_game.pop(i)
                    score += 1

                if player_rect.colliderect(el):
                    gameplay = False

        if wolf_list_in_game:
            for i, el in enumerate(wolf_list_in_game):
                screen.blit(wolf_left[player_anim_count], el)
                el.x -= 20
                if el.x < -10:
                    wolf_list_in_game.pop(i)
                    score += 1

                if player_rect.colliderect(el):
                    gameplay = False

        if bird_list_in_game:
            for i, el in enumerate(bird_list_in_game):
                screen.blit(bird_left[player_anim_count], el)
                el.x -= 25
                if el.x < -10:
                    bird_list_in_game.pop(i)
                    score += 1

                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 500:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_UP]:
                is_jump = True
        else:
            if jump_count >= -10:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 10
        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1
        bg_x -= 2

        if bg_x == -1000:
            bg_x = 0

        if bullets:
            for i, el in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 30

                if el.x > 1050:
                    bullets.pop(i)
                if flower_list_in_game:
                    for index, flower in enumerate(flower_list_in_game):
                        if el.colliderect(flower):
                            flower_list_in_game.pop(index)
                            bullets.pop(i)
                            score += 1

                if wolf_list_in_game:
                    for index, wolf in enumerate(wolf_list_in_game):
                        if el.colliderect(wolf):
                            wolf_list_in_game.pop(index)
                            bullets.pop(i)
                            score += 1

                if bird_list_in_game:
                    for index, bird in enumerate(bird_list_in_game):
                        if el.colliderect(bird):
                            bird_list_in_game.pop(index)
                            bullets.pop(i)
                            score += 1

        if score % 5 == 0 and score != 0:
            bullet_left += 1
            score += 1


    else:
        screen.fill((189, 45, 34))
        screen.blit(lose_lable, (400, 300))
        screen.blit(score_lable, (100, 300))
        screen.blit(restart_lable, restart_lable_rect)

        mouse = pygame.mouse.get_pos()

        if restart_lable_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 300
            flower_list_in_game.clear()
            wolf_list_in_game.clear()
            bird_list_in_game.clear()
            bullets.clear()
            bullet_left = 5
            score = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == flower_timer:
            flower_list_in_game.append(enemy_left[0].get_rect(topleft=(1060, 430)))
        if event.type == wolf_timer:
            wolf_list_in_game.append(wolf_left[0].get_rect(topleft=(1060, 430)))
        if event.type == bird_timer:
            bird_list_in_game.append(bird_left[0].get_rect(topleft=(1060, 250)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and bullet_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 28)))
            bullet_left -= 1
    clock.tick(20)
