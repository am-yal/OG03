import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('image/cb6ee242896180d920c425ffbf84cf77.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('image/target.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

score = 0
font = pygame.font.Font(None, 28)

target_speed_x = random.choice([-0.1, 0.1])
target_speed_y = random.choice([-0.1, 0.1])

start_time = time.time()

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 100
    target_x += target_speed_x
    target_y += target_speed_y
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y
    screen.blit(target_img, (target_x, target_y))
    score_text = font.render('Очки: ' + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    elapsed_time = time.time() - start_time
    time_text = font.render('Время: {:.1f} сек'.format(elapsed_time), True, (0, 0, 0))
    screen.blit(time_text, (10, 50))
    if score >= 1000:
        congrats_text = font.render(f'Поздравляем! Вы набрали максимальное количество очков всего за {elapsed_time:.3f}!', True, (255, 0, 0))
        screen.blit(congrats_text, (50, SCREEN_HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    pygame.display.update()

pygame.quit()