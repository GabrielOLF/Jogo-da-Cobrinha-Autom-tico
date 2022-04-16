import pygame
import random

pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake Game')
game_over=False
blue=(0,0,255)
red=(255,0,0)
apple_position_x = 100
apple_position_y = 200
points = 0
x1 = 200
y1 = 150 
x1_change = 0       
y1_change = 0
snake_list = []
snake_len = 1
snake_speed_default = 3

def snake(snake_list):
    for piece in snake_list:
        player_rect = pygame.draw.rect(dis, blue, [piece[0], piece[1], 10, 10]) 
    return player_rect
FPS_TICK = 60
clock = pygame.time.Clock()
white = (255, 255, 255)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if x1 > apple_position_x:
        x1 -= 5
    if y1 > apple_position_y:
        y1 -= 5
    if x1 < apple_position_x:
        x1 += 5
    if y1 < apple_position_y:
        y1 += 5
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > snake_len:
        del snake_list[0]
    if x1 >= 400:
        x1 -= 400
    if x1 <= 0:
        x1 += 400
    if y1 >= 300:
        y1 -= 300
    if y1 <= 0:
        y1 += 300
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    apple_rect = pygame.draw.rect(dis,red,[apple_position_x, apple_position_y,10,10])
    player_1 = snake(snake_list)
    if  pygame.Rect.colliderect(player_1, apple_rect) == True:
        points += 1
        snake_speed_default += 0.03
        snake_len += 1
        apple_position_x = random.choice(range(0, 380))
        apple_position_y = random.choice(range(0, 280))
        

    if points == 0:
        pygame.draw.rect(dis,red,[apple_position_x, apple_position_y,10,10])



    pygame.display.update()
    clock.tick(FPS_TICK)
pygame.quit()
quit()
