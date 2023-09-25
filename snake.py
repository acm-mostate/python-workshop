#!/usr/bin/env python3
import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Screen dimensions
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20

# Screen and clock setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, pygame.Rect(food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = (1, 0)
    food = (random.randint(0, (WIDTH//CELL_SIZE) - 1), random.randint(0, (HEIGHT//CELL_SIZE) - 1))
    
    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        head = snake[0]
        new_head = ((head[0] + direction[0]) % (WIDTH//CELL_SIZE), (head[1] + direction[1]) % (HEIGHT//CELL_SIZE))
        snake.insert(0, new_head)
        if new_head == food:
            food = (random.randint(0, (WIDTH//CELL_SIZE) - 1), random.randint(0, (HEIGHT//CELL_SIZE) - 1))
        else:
            snake.pop()

        if len(snake) != len(set(snake)):
            running = False

        draw_snake(snake)
        draw_food(food)
        
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == '__main__':
    main()
