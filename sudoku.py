from sudoku_generator import *
from constants import *
import pygame
from cell import Cell
from Button import *
from board import Board
from welcome import *

pygame.init()
pygame.display.set_caption("Sudoko")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
board = None
user_font = pygame.font.Font(None, USERADD_FONT)


def get_row_col(x, y):
    list = [0, 66, 133, 199, 266, 333, 399, 466, 533, 600]
    for i in range(0, 9):
        if x in range(list[i], list[i + 1]):
            col = i
    for index in range(0, 9):
        if y in range(list[index], list[index + 1]):
            row = index
    return row, col

def get_cell(pos, cells):
    for e in cells:
        if pos == e.get_pos():
            return e

def compare_values(value, cell):
    if value == cell.get_value():
        return True
    return False

def get_pressed_num(key):
    if key == pygame.K_1:
        return 1
    elif key == pygame.K_2:
        return 2
    elif key == pygame.K_3:
        return 3
    elif key == pygame.K_4:
        return 4
    elif key == pygame.K_5:
        return 5
    elif key == pygame.K_6:
        return 6
    elif key == pygame.K_7:
        return 7
    elif key == pygame.K_8:
        return 8
    elif key == pygame.K_9:
        return 9



"""all the button stuff right here"""



screen.fill(BG_COLOR)

# initializes welcome
welcome()
game_start = False
input_numbers = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
while True:
    MOUSE_POSITION = pygame.mouse.get_pos()  # I need to organize this better
    for event in pygame.event.get():  # Every time you click on a sudoku square, the options disappear. Think it has something to do with loop

        if event.type == pygame.QUIT:
            pygame.quit()

        elif game_start == False:
            Button.check_if_hover(EASY_BUTTON)
            Button.check_if_hover(MEDIUM_BUTTON)
            Button.check_if_hover(HARD_BUTTON)

        else:
            # for event, after player has chosen mode
            Button.check_if_hover(RESET_BUTTON)
            Button.check_if_hover(RESTART_BUTTON)
            Button.check_if_hover(EXIT_BUTTON)

        if event.type == pygame.MOUSEBUTTONDOWN:

            if game_start == False:
                if EASY_BUTTON.rectangle.collidepoint(MOUSE_POSITION):  # player clicks easy
                    print("easy mode activated ")
                    board = Board(9, 9, screen, "easy")
                    screen.fill(BG_COLOR)
                    board.draw()
                    game_start = True

                elif MEDIUM_BUTTON.rectangle.collidepoint(MOUSE_POSITION):  # player clicks medium
                    print("medium mode activated ")
                    board = Board(9, 9, screen, "medium")
                    screen.fill(BG_COLOR)
                    board.draw()
                    game_start = True

                elif HARD_BUTTON.rectangle.collidepoint(MOUSE_POSITION):  # player clicks hard
                    print("hard mode activated ")
                    board = Board(9, 9, screen, "hard")
                    screen.fill(BG_COLOR)
                    board.draw()
                    game_start = True
            else:
                if RESET_BUTTON.rectangle.collidepoint(MOUSE_POSITION):  # player clicks reset
                    print("reset the game")

                elif RESTART_BUTTON.rectangle.collidepoint(MOUSE_POSITION):  # player clicks restart
                    print("restart the game")
                    game_start = False
                    welcome()
                    # takes back to menu screen
                elif EXIT_BUTTON.rectangle.collidepoint(MOUSE_POSITION):  # player clicks exit
                    pygame.quit()
            if game_start == True:
                # player has chosen a mode from menu
                x, y = event.pos
                row = y // CHIP_SIZE
                col = x // CHIP_SIZE
                cur_row, cur_col = get_row_col(x, y)
                print(row, col)
        if event.type == pygame.KEYDOWN:
            if game_start == True:
                if event.key in input_numbers:
                    print(get_pressed_num(event.key))
                    print(board.final_board[row][col])
                    if str(get_pressed_num(event.key)) == board.final_board[row][col]:
                        print("TRUE")
            if event.key == pygame.K_UP:
                row -= 1
                if cur_row == -1:
                    cur_row = 8
                print(row)
            elif event.key == pygame.K_DOWN:
                cur_row += 1
                if cur_row == 9:
                    cur_row = 0
            elif event.key == pygame.K_LEFT:
                cur_col -= 1
                if cur_col == -1:
                    cur_col = 8
            elif event.key == pygame.K_RIGHT:
                cur_col += 1
                if cur_col == 9:
                    cur_col = 0
            elif event.key == pygame.K_RETURN:
                print(cur_input_allowed)

    pygame.display.update()

