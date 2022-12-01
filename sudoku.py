from sudoku_generator import *
from constants import *
import pygame

pygame.init()

pygame.display.set_caption("Sudoko")


screen = pygame.display.set_mode((WIDTH, HEIGHT))

board = SudokuGenerator(9, 10)
board.fill_values()
board.print_board()
full_board = board.get_board()
board.remove_cells()
user_board = board.get_board()





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








class Button():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    button_font = pygame.font.Font(None, 30)
    
    def __init__(self, surface, fill_color, text_message, rectangle, og_color, hover_color):
        self.surface = surface


        self.fill_color = fill_color
        self.text_message = text_message
        self.rectangle = rectangle 
        self.og_color = og_color
        self.hover_color = hover_color

        
    def display(self):
        self.text = button_font.render(self.text_message, 0, self.og_color)

        self.surface.fill(self.fill_color)

        self.surface.blit(self.text, (10,10))
        screen.blit(self.surface, self.rectangle)

    def check_if_hover(self):
        MOUSE_POSITION = pygame.mouse.get_pos()

        if self.rectangle.collidepoint(MOUSE_POSITION):
            self.text = button_font.render(self.text_message, 0, (self.hover_color))
            self.surface.blit(self.text, (10,10))
            screen.blit(self.surface, self.rectangle)
        else:
            Button.display(self)

"""all the button stuff right here"""
button_font = pygame.font.Font(None, 40)

#easy button
easy_text = button_font.render("EASY", 0, (100, 200, 40))
easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))

#medium button
medium_text = button_font.render("MEDIUM", 0, (30, 5, 255))
medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))

#hard button
hard_text = button_font.render("HARD", 0, (200, 9, 9))
hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))

#Reset button
reset_text = button_font.render("RESET", 0, (255,0,2))
reset_surface = pygame.Surface((reset_text.get_size()[0] + 10, reset_text.get_size()[1] + 10))

#Restart button
restart_text = button_font.render("RESTART,", 0, (255,0,2))
restart_surface = pygame.Surface((restart_text.get_size()[0] + 55, restart_text.get_size()[1] + 55))

#Exit button
exit_text = button_font.render("EXIT,", 0, (255,0,2))
exit_surface = pygame.Surface((exit_text.get_size()[0] + 10, exit_text.get_size()[1] + 10))


""" MODES """
EASY_BUTTON = Button(surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20)), fill_color = LINE_COLOR, text_message = "EASY" , rectangle = easy_surface.get_rect(
    center=(WIDTH // 5.5, HEIGHT //2 + 50)), og_color = (100, 200, 40), hover_color = (255,25,255) )
MEDIUM_BUTTON = Button(surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20)), fill_color = LINE_COLOR, text_message = "MEDIUM" , rectangle = medium_surface.get_rect(
    center=(WIDTH // 2, HEIGHT //2 + 50)), og_color = (30, 5, 255), hover_color = (255,25,255) )
HARD_BUTTON = Button(surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20)), fill_color = LINE_COLOR, text_message = "HARD" , rectangle =  hard_surface.get_rect(
    center=(WIDTH // 1.22, HEIGHT // 2 + 50)), og_color = (200, 9, 9), hover_color = (255,25,255) )

""" OPTIONS """
RESET_BUTTON = Button(surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20)), fill_color = OPTION_COLOR, text_message = "RESET", rectangle = reset_surface.get_rect(
        center=(WIDTH // 5.5, HEIGHT // 2 + 298.7)),og_color = BG_COLOR, hover_color = (255,25,255))
RESTART_BUTTON = Button(surface = pygame.Surface((reset_text.get_size()[0] + 55, reset_text.get_size()[1] + 55)), fill_color = OPTION_COLOR, text_message = "RESTART", rectangle = reset_surface.get_rect(
        center=(WIDTH // 2.1, HEIGHT // 2 + 298.7)),og_color = BG_COLOR, hover_color = (255,25,255)) 
EXIT_BUTTON = Button(surface = pygame.Surface((exit_text.get_size()[0] + 12, exit_text.get_size()[1] + 20)), fill_color = OPTION_COLOR, text_message = "EXIT", rectangle = exit_surface.get_rect(
        center=(WIDTH // 1.22, HEIGHT // 2 + 298.7)),og_color = BG_COLOR, hover_color = (255,25,255)) 

def welcome():
    welcome_message_font = pygame.font.Font(None,82)

    #Big welcome message at top
    screen.fill(BG_COLOR)
    welcome_surface = welcome_message_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    welcome_rectangle = welcome_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 201))
    #initializes welcome 
    screen.blit(welcome_surface, welcome_rectangle)
    

    select_message = f"Select Game Mode:"
    select_message_font = pygame.font.Font(None,60)
    select_surf = select_message_font.render(select_message, 0, LINE_COLOR)
    select_rect = select_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

    #initializes select message
    screen.blit(select_surf, select_rect)

def sketch():
    for row in range(board.row_length):
        for col in range(board.row_length):
            if user_board[row][col] == 0:
                number_surf = user_font.render("", 0, ADDED_COLOR)
            else:
                number_surf = user_font.render(str(user_board[row][col]), 0, ADDED_COLOR)
            number_rect = number_surf.get_rect(center= (CHIP_SIZE * col + CHIP_SIZE // 2, CHIP_SIZE * row + CHIP_SIZE // 2))
            screen.blit(number_surf, number_rect)
screen.fill(BG_COLOR)

#initializes welcome
welcome()
game_start = False
while True:
    MOUSE_POSITION = pygame.mouse.get_pos()           #I need to organize this better 
    for event in pygame.event.get():                 # Every time you click on a sudoku square, the options disappear. Think it has something to do with loop
                                                     
       
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
                if EASY_BUTTON.rectangle.collidepoint(MOUSE_POSITION): # player clicks easy 
                    print("easy mode activated ")              
                    game_start = True
                    
                elif MEDIUM_BUTTON.rectangle.collidepoint(MOUSE_POSITION): # player clicks medium
                    print("medium mode activated ")
                    game_start = True

                elif HARD_BUTTON.rectangle.collidepoint(MOUSE_POSITION): # player clicks hard
                    print("hard mode activated ")
                    game_start = True
            else:
                if RESET_BUTTON.rectangle.collidepoint(MOUSE_POSITION): # player clicks reset
                    print("reset the game")
                elif RESTART_BUTTON.rectangle.collidepoint(MOUSE_POSITION): # player clicks restart
                    print("restart the game")
                    game_start = False
                    welcome() 
                    #takes back to menu screen
                elif EXIT_BUTTON.rectangle.collidepoint(MOUSE_POSITION): # player clicks exit
                    pygame.quit()
                    
            if game_start == True:
                #player has chosen a mode from menu
                screen.fill(BG_COLOR)    

                draw_game()
                sketch()   
            x, y = event.pos
            print(x,y)

    pygame.display.update()
        
    