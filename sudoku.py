from sudoku_generator import *
import pygame
from Button import *
from board import Board
from welcome import *

pygame.init()
pygame.display.set_caption("Sudoko")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
board = None
input_num = 0
user_font = pygame.font.Font(None, USERADD_FONT)

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

screen.fill(BG_COLOR)

# initializes welcome
welcome()

press_return = False
sketched_nums_before_return = []

game_start = False
input_numbers = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
while True:
    MOUSE_POSITION = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif game_start == False:
            Button.check_if_hover(EASY_BUTTON)
            Button.check_if_hover(MEDIUM_BUTTON)
            Button.check_if_hover(HARD_BUTTON)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_start == False:
                if EASY_BUTTON.rectangle.collidepoint(MOUSE_POSITION):  # player clicks easy
                    print("easy mode activated ")
                    board = Board(9, 9, screen, "easy")

                elif MEDIUM_BUTTON.rectangle.collidepoint(MOUSE_POSITION):  # player clicks medium
                    print("medium mode activated ")
                    board = Board(9, 9, screen, "medium")

                elif HARD_BUTTON.rectangle.collidepoint(MOUSE_POSITION):  # player clicks hard
                    print("hard mode activated ")
                    board = Board(9, 9, screen, "hard")

                board.draw()
                game_start = True
                first_click = True # to make sure no cell is selected after clicking game mode
            else:
                if RESET_BUTTON.rectangle.collidepoint(MOUSE_POSITION):  # player clicks reset
                    print("reset the game")
                    for i in board.empty_cells:
                        row = i[0]
                        col = i[1]
                        board.clear(row, col)
                    board.sketched_nums = []
                    board.draw()

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
               
                '''box highlight and floating numbers'''
                board.draw()

                Button.check_if_hover(RESET_BUTTON)
                Button.check_if_hover(RESTART_BUTTON)
                Button.check_if_hover(EXIT_BUTTON)

                if first_click == False:   
                    board.highlight_box(col, row)
                first_click = False

                if press_return == False:
                
                    current_sketched_nums = []

                    for sketched_nums in board.sketched_nums:
                        current_sketched_nums.append(sketched_nums)
                    if current_sketched_nums != []:
                        sketched_nums_before_return.append(current_sketched_nums[-1]) # returns last sketch value if user is shuffling through numbers
                        current_input_num = current_sketched_nums[-1][0]
                        current_row = current_sketched_nums[-1][1]
                        current_col = current_sketched_nums[-1][2] 
                    
                    for i in sketched_nums_before_return:
                        c_input_num = i[0]
                        c_row = i[1]
                        c_col = i[2]

                        board.sketch(c_input_num, c_row, c_col, BG_COLOR)

                        board.sketch(c_input_num, c_row, c_col, USERADD_COLOR)
 
                if press_return == True:
                    sketched_nums_before_return = []
                    press_return = False


        if event.type == pygame.KEYDOWN:
            if game_start == True:
                if event.key in input_numbers and board.final_board[row][col] == 0: #Checks to see if space is available
                    if board.click(row, col) != None:
                        #Sketches number in
                        board.sketch(input_num, row, col, BG_COLOR)
                        input_num = str(get_pressed_num(event.key))
                        board.sketched_nums.append([input_num, row, col])
                        # print(board.sketched_nums)
                        board.sketch(input_num, row, col, USERADD_COLOR)
                        
                    else:
                        pass
            if event.key == pygame.K_UP:
                row -= 1
                if row == -1:
                    cur_row = 8
                board.highlight_box(col, row)
            elif event.key == pygame.K_DOWN:
                row += 1
                if row == 9:
                    row = 0
                board.highlight_box(col, row)
            elif event.key == pygame.K_LEFT:
                col -= 1
                if col == -1:
                    col = 8
                board.highlight_box(col, row)
            elif event.key == pygame.K_RIGHT:
                col += 1
                if col == 9:
                    col = 0
                board.highlight_box(col, row)
            elif event.key == pygame.K_RETURN:
                #Fully inputs sketched numbers into board

                press_return = True
                for i in board.sketched_nums:
                    board.final_board[i[1]][i[2]] = i[0]
                    board.draw()
                    board.sketched_nums = []


                    #Check if board is filled
                    if board.is_full():
                        print(board.check_board())
                    
                else:
                    pass
            elif event.key == pygame.K_BACKSPACE:
                #Reset cell and upate board
                cell = [row,col]
                if cell in board.empty_cells:
                    board.clear(row, col)
                    board.draw()
                    


    pygame.display.update()

