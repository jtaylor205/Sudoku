import pygame
from constants import *
from sudoku_generator import SudokuGenerator
from cell import Cell
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
user_font = pygame.font.Font(None, USERADD_FONT)
class Board:
    full_board = None #Board completely filled
    final_board = None #Board that is edited as the user plays the game
    def __init__(self, width, height, screen, difficulty): #Initialize and create the board
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.empty_cells = []
        self.sketched_nums = []
        if self.difficulty == "easy":
            self.sudo = SudokuGenerator(9, 30)
            pass
        elif self.difficulty == "medium":
            self.sudo = SudokuGenerator(9, 40)
            pass
        elif self.difficulty == "hard":
            self.sudo = SudokuGenerator(9, 50)
            pass
        self.sudo.fill_values()
        self.sudo.get_board()
        self.full_board = self.sudo.print_board()
        self.sudo.remove_cells()
        self.final_board = self.sudo.get_board()

    def draw(self):
        #Draw out the board lines and also draw each cell
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

        for row in range(self.width):
            for col in range(self.height):
                if self.final_board[row][col] == 0:
                    empty_cell = [row, col]
                    self.empty_cells.append(empty_cell)
                new_cell = Cell(self.final_board[row][col], row, col, screen)
                new_cell.draw()

                
    def click(self, x, y):
        #Check if location is a box
        if x < self.width and y < self.height:
            return (x, y)
        else:
            return None

    def is_full(self):
        #Check if user has filled out board
        for row in range(self.width):
            for col in range(self.height):
                if self.final_board[row][col] == 0:
                    return False
                else:
                    continue
        return True

    def check_board(self):
        #Check if the board is a solved sudoku
        for row in range(self.width):
            for col in range(self.height):
                if str(self.final_board[row][col]) == str(self.full_board[row][col]):
                    continue
                else:
                    return False
        return True

    def clear(self, row, col):
        self.final_board[row][col] = 0

    def sketch(self, value, row, col, color):
        #Sketch value into the board

        number_surf = user_font.render(str(value), 0, color)
        number_rect = number_surf.get_rect(
            center=(CHIP_SIZE * col + CHIP_SIZE // 2 - 15, CHIP_SIZE * row + CHIP_SIZE // 2 - 15))
        self.screen.blit(number_surf, number_rect)

    def highlight_box(self, col, row):
        self.row = row
        self.col = col
        
        if row < 9:
            red_square = pygame.draw.rect(screen, (255,0,0), ((col * 67) - 1.25, (row * 67) -0.1, 68, 66.5), 3)
        else:
            red_square = None
        return red_square

   