import pygame
import time

pygame.init()

display_width = 1000
display_height = 800
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

grass_color = (124, 252, 0)
snake_color = (255, 127, 80)
lost_color = (255, 0, 0)

x = display_width/2
y = display_height/2

snake_size = 20

clock = pygame.time.Clock()
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width/2, display_height/2])


x_change = 0
y_change = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_speed
                y_change = 0
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = snake_speed
            elif event.key == pygame.K_RIGHT:
                x_change = snake_speed
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -snake_speed

    if x >= display_width or x < 0 or y >= display_height or y < 0:
            game_over = True

    x += x_change
    y += y_change

    display.fill(grass_color)
    pygame.draw.rect(display, snake_color, [x, y, snake_size, snake_size])
    pygame.display.update()

    clock.tick(snake_speed)


message("You lost", lost_color)
pygame.display.update()
time.sleep(3)

pygame.quit()
quit()
