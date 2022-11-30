from sudoku_generator import SudokuGenerator
from constants import *
import pygame

pygame.init()

pygame.display.set_caption("Sudoko")

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_game():
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE),(WIDTH, SQUARE_SIZE), LINE_WIDTH)

screen.fill(BG_COLOR)
draw_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

