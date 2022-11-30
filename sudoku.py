from sudoku_generator import SudokuGenerator
import pygame

pygame.init()

pygame.display.set_caption("Sudoko")

screen = pygame.display.set_mode((350, 350))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

#OK