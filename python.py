import pygame
import time
import random

pygame.init()

# Game window dimensions
width, height = 800, 600
game_display = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Initial snake properties
snake_size = 10
snake_speed = 15

clock = pygame.time.Clock()

# Score function
def your_score(score):
    font = pygame.font.SysFont(None, 35)
    text = font.render('Score: ' + str(score), True, white)
    game_display.blit(text, [0, 0])

# Snake function
def our_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_pixels = []
    snake_length = 1

    foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(black)
            your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_size
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_size

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_display.fill(black)
        pygame.draw.rect(game_display, white, [foodx, foody, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_pixels.append(snake_head)
        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == snake_head:
                game_close = True

        our_snake(snake_size, snake_pixels)
        your_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
