import pygame
from constants import *
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
button_font = pygame.font.Font(None, 40)

# easy button
easy_text = button_font.render("EASY", 0, (100, 200, 40))
easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))

# medium button
medium_text = button_font.render("MEDIUM", 0, (30, 5, 255))
medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))

# hard button
hard_text = button_font.render("HARD", 0, (200, 9, 9))
hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))

# Reset button
reset_text = button_font.render("RESET", 0, (255, 0, 2))
reset_surface = pygame.Surface((reset_text.get_size()[0] + 10, reset_text.get_size()[1] + 10))

# Restart button
restart_text = button_font.render("RESTART,", 0, (255, 0, 2))
restart_surface = pygame.Surface((restart_text.get_size()[0] + 55, restart_text.get_size()[1] + 55))

# Exit button
exit_text = button_font.render("EXIT,", 0, (255, 0, 2))
exit_surface = pygame.Surface((exit_text.get_size()[0] + 10, exit_text.get_size()[1] + 10))

def welcome():
    welcome_message_font = pygame.font.Font(None, 82)
    # Big welcome message at top
    screen.fill(BG_COLOR)
    welcome_surface = welcome_message_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    welcome_rectangle = welcome_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 201))
    # initializes welcome
    screen.blit(welcome_surface, welcome_rectangle)
    select_message = f"Select Game Mode:"
    select_message_font = pygame.font.Font(None, 60)
    select_surf = select_message_font.render(select_message, 0, LINE_COLOR)
    select_rect = select_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    # initializes select message
    screen.blit(select_surf, select_rect)