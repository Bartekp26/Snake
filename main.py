import pygame
import random

pygame.init()

# Window
display_width = 1000
display_height = 800
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

# Colors
grass_color = (124, 252, 0)
snake_color = (161, 165, 140)
red = (255, 0, 0)
yellow = (255, 255, 105)
white = (255, 255, 255)

# Snake
snake_size = 25
snake_speed = 20

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    display.blit(value, [10, 10])


def our_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, snake_color, [x[0], x[1], snake_size, snake_size])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width/6, display_height/3])


def game_loop():
    game_over = False
    game_close = False

    x = display_width / 2
    y = display_height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            display.fill(white)
            message("You lost! Press Q (quit) or C (play again)", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

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
            game_close = True

        x += x_change
        y += y_change

        display.fill(grass_color)
        pygame.draw.rect(display, red, [food_x, food_y, snake_size, snake_size])

        snake_head = list()
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        our_snake(snake_size, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if  food_x-snake_size < x < food_x+snake_size and food_y-snake_size < y < food_y+snake_size:
            food_x = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - snake_size) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
