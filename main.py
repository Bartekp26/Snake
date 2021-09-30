import pygame

pygame.init()

display_width = 1000
display_height = 800
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

grass_color = (124, 252, 0)
snake_color = (255,127,80)

x = display_width/2
y = display_height/2

clock = pygame.time.Clock()

game_over = False
while not game_over:
    for event in pygame.event.get():
        x_change = 0
        y_change = 0

        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
            elif event.key == pygame.K_DOWN:
                y_change = 10
            elif event.key == pygame.K_RIGHT:
                x_change = 10
            elif event.key == pygame.K_UP:
                y_change = -10

        x += x_change
        y += y_change

        display.fill(grass_color)
        pygame.draw.rect(display, snake_color, [x, y, 20, 20])
        pygame.display.update()


pygame.quit()
quit()
