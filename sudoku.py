from sudoku_generator import *
from constants import *
import pygame

pygame.init()

pygame.display.set_caption("Sudoko")

screen = pygame.display.set_mode((WIDTH, HEIGHT))

board = SudokuGenerator(9, 0)
board.fill_values()
board.remove_cells()
user_board = SudokuGenerator(9, 0)

user_font = pygame.font.Font(None, USERADD_FONT)
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




def sketch():
    for row in range(board.row_length):
        for col in range(board.row_length):
            number_surf = user_font.render(str(board.board[row][col]), 0, ADDED_COLOR)
            number_rect = number_surf.get_rect(center= (CHIP_SIZE * col + CHIP_SIZE // 2, CHIP_SIZE * row + CHIP_SIZE // 2))
            screen.blit(number_surf, number_rect)
screen.fill(BG_COLOR)
draw_game()
sketch()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

