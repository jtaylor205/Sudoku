from sudoku_generator import SudokuGenerator
from constants import *
import pygame

pygame.init()

pygame.display.set_caption("Sudoko")

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_game():
    #Draw defining borders
    for i in range(1, BOARD_ROWS):
        for j in range(1, BOARD_ROWS * 2):
            pygame.draw.line(screen, LINE_COLOR, (0, (j * i * SQUARE_SIZE)/3), (WIDTH, (j * i * SQUARE_SIZE)/3), 2)
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
    for i in range(1, BOARD_COLS):
        for j in range(1, BOARD_COLS * 2):
            pygame.draw.line(screen, LINE_COLOR, ((j * i * SQUARE_SIZE)/3,0), ((j * i * SQUARE_SIZE)/3, WIDTH), 2)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, WIDTH), LINE_WIDTH)



screen.fill(BG_COLOR)
draw_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

