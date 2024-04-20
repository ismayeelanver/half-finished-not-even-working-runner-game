import pygame, os
from sys import exit

pygame.init()

w = 800
h = 400
cwd = os.getcwd() + "/Runner"
pygame.display.set_caption('Game')
font = pygame.font.Font("Runner/fonts/normal.ttf", 64)
bg = pygame.image.load("Runner/Bg.png")
ground = pygame.image.load("Runner/ground.png")
pipe1 = pygame.image.load("Runner/pipes/pipe.png")
pipe1_x_pos = 600
spider = pygame.image.load("Runner/enemies/spider.png")
spider_x_pos = 300
player = pygame.image.load("Runner/player/maio.png")
maio_x_pos = 100
maio_y_pos = 240
screen = pygame.display.set_mode((w,h))
running = True
while running:
    pygame.display.update()
    screen.blit(bg, (0,0))
    screen.blit(ground, (0,300))
    screen.blit(pipe1, (pipe1_x_pos,180))
    screen.blit(spider, (spider_x_pos,250))
    screen.blit(player, (maio_x_pos, maio_y_pos))
    maio_x_pos += 4
    if maio_x_pos > 800: maio_x_pos = -100
    spider_x_pos -= 4
    if spider_x_pos < -100: spider_x_pos = 800
    pipe1_x_pos -= 4
    if pipe1_x_pos < -100: pipe1_x_pos = 800
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        maio_y_pos -= 20

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.time.Clock().tick(60)