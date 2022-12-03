import pygame
from constants import *
from sudoku_generator import SudokuGenerator
from cell import Cell
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
class Board:
    final_board = None
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        if self.difficulty == "easy":
            self.sudo = SudokuGenerator(9, 30)
            pass
        elif self.difficulty == "medium":
            self.sudo = SudokuGenerator(9, 40)
            pass
        elif self.difficulty == "hard":
            self.sudo = SudokuGenerator(9, 50)
            pass

    def draw(self):
        screen.fill(BG_COLOR)
        for i in range(1, BOARD_ROWS):
            for j in range(1, BOARD_ROWS * 2):
                pygame.draw.line(self.screen, LINE_COLOR, (0, (j * i * SQUARE_SIZE) / 3), (WIDTH, (j * i * SQUARE_SIZE) / 3),
                                 2)
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        for i in range(1, BOARD_COLS):
            for j in range(1, BOARD_COLS * 2):
                pygame.draw.line(self.screen, LINE_COLOR, ((j * i * SQUARE_SIZE) / 3, 0), ((j * i * SQUARE_SIZE) / 3, WIDTH),
                                 2)
            pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, WIDTH), LINE_WIDTH)

        self.sudo.fill_values()
        self.final_board = self.sudo.get_board()
        self.sudo.print_board()
        self.sudo.remove_cells()
        for row in range(self.width):
            for col in range(self.height):
                new_cell = Cell(self.user_board[row][col], row, col, screen)
                new_cell.draw()

    def select(self, row, col):
        return

    def click(self, x, y):
        if x < self.width and y < self.height:
            return (x, y)
        else:
            return None
