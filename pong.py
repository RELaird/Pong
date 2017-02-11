import pygame
import sys
from pygame.locals import *

pygame.init()

background_image_filename = 'Background.jpg'
SCREEN_SIZE = (800, 480)
paddle_size = (7,30)
white = (255,255,255)

right_paddle_x = 700
right_paddle_y = SCREEN_SIZE[1]/2 - (paddle_size[1]/2)
left_paddle_x = 100
left_paddle_y = SCREEN_SIZE[1]/2 - (paddle_size[1]/2)
move_right_paddle_y = 0
move_left_paddle_y = 0

screen = pygame.display.set_mode((SCREEN_SIZE), 0, 32)
pygame.display.set_caption("Pong")

background = pygame.image.load(background_image_filename).convert()
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                move_right_paddle_y = -1
            elif event.key == K_DOWN:
                move_right_paddle_y = +1
            if event.key == K_w:
                move_left_paddle_y = -1
            elif event.key == K_s:
                move_left_paddle_y = +1
        if event.type == KEYUP:
            if event.key == K_UP:
                move_right_paddle_y = 0
            elif event.key == K_DOWN:
                move_right_paddle_y = 0
            if event.key == K_w:
                move_left_paddle_y = 0
            elif event.key == K_s:
                move_left_paddle_y = 0

    screen.blit(background, (0,0))

    right_paddle_y += move_right_paddle_y
    left_paddle_y += move_left_paddle_y
    right_paddle_pos = (right_paddle_x, right_paddle_y)
    left_paddle_pos = (left_paddle_x, left_paddle_y)
    pygame.draw.rect(screen, white, Rect(right_paddle_pos, paddle_size))
    pygame.draw.rect(screen, white, Rect(left_paddle_pos, paddle_size))

    pygame.display.update()
