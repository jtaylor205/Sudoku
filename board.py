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
                new_cell = Cell(self.final_board[row][col], row, col, screen)
                new_cell.draw()

<<<<<<< HEAD
                
=======
    def select(self, row, col):
        return

>>>>>>> 37dc82593b2fe0f79570ef37590f1fc93a17b238
    def click(self, x, y):
        if x < self.width and y < self.height:
            return (x, y)
        else:
            return None

    def is_full(self):
        for row in range(self.width):
            for col in range(self.height):
                if self.final_board[row][col] == 0:
                    return False
                else:
                    continue
<<<<<<< HEAD
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

   
=======
        return True
>>>>>>> 37dc82593b2fe0f79570ef37590f1fc93a17b238
