#!/usr/bin/env python3
import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Colors
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK = (74, 127, 198)
WHITE = (255, 255, 255)  # Color for displaying the score

# Screen dimensions
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simple Snake Game with Score')
clock = pygame.time.Clock()

def start_screen():
    """Display the starting screen."""
    while True:
        screen.fill(BLACK)
        
        font = pygame.font.SysFont(None, 50)
        title_text = font.render("Welcome to Snake Game", True, WHITE)
        instruction_text = font.render("Press ENTER to Start", True, WHITE)
        
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - title_text.get_height()))
        screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2 + 20))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return  # Exit the start screen loop and start the game


def game_over_display(score):
    """Display a game over screen with the score."""
    while True:
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 50)
        game_over_text = font.render("Game Over", True, RED)
        score_text = font.render(f"Score: {score}", True, WHITE)
        
        restart_text = font.render("Press 'R' to Restart", True, WHITE)
        quit_text = font.render("Press 'Q' to Quit", True, WHITE)
        
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + game_over_text.get_height()))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + game_over_text.get_height() + score_text.get_height() + 10))
        screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + game_over_text.get_height() + score_text.get_height() + restart_text.get_height() + 20))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                main()  # Restart the game

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, pygame.Rect(food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_score(score):
    font = pygame.font.SysFont(None, 35)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def main():
    start_screen()
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = (1, 0)
    food = (random.randint(0, (WIDTH//CELL_SIZE) - 1), random.randint(0, (HEIGHT//CELL_SIZE) - 1))
    score = 0

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT:
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    direction = (1, 0)

        head = snake[0]
        print(snake)
        new_head = ((head[0] + direction[0]) , (head[1] + direction[1]) )
        
        snake.insert(0, new_head)
        if new_head == food:
            food = (random.randint(0, (WIDTH//CELL_SIZE) - 1), random.randint(0, (HEIGHT//CELL_SIZE) - 1))
            score += 1  # Increase the score when food is eaten
        else:
            snake.pop()

        if new_head in snake[1:]:
            running = False
        
        draw_snake(snake)
        draw_food(food)
        draw_score(score)  # Display the score

        
        pygame.display.flip()
        clock.tick(10)
    game_over_display(score)
    pygame.quit()

if __name__ == '__main__':
    main()
