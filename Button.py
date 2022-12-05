from constants import *
import pygame
from welcome import *
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
button_font = pygame.font.Font(None, 40)
class Button():
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
        self.surface.blit(self.text, (10, 10))
        screen.blit(self.surface, self.rectangle)

    def check_if_hover(self):
        MOUSE_POSITION = pygame.mouse.get_pos()

        if self.rectangle.collidepoint(MOUSE_POSITION):
            self.text = button_font.render(self.text_message, 0, (self.hover_color))
            self.surface.blit(self.text, (10, 10))
            screen.blit(self.surface, self.rectangle)
        else:
            Button.display(self)

""" MODES """
EASY_BUTTON = Button(surface=pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20)),
                     fill_color=LINE_COLOR, text_message="EASY", rectangle=easy_surface.get_rect(
        center=(WIDTH // 5.5, HEIGHT // 2 + 50)), og_color=(100, 200, 40), hover_color=(255, 25, 255))
MEDIUM_BUTTON = Button(surface=pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20)),
                       fill_color=LINE_COLOR, text_message="MEDIUM", rectangle=medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 50)), og_color=(30, 5, 255), hover_color=(255, 25, 255))
HARD_BUTTON = Button(surface=pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20)),
                     fill_color=LINE_COLOR, text_message="HARD", rectangle=hard_surface.get_rect(
        center=(WIDTH // 1.22, HEIGHT // 2 + 50)), og_color=(200, 9, 9), hover_color=(255, 25, 255))

""" OPTIONS """
RESET_BUTTON = Button(surface=pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20)),
                      fill_color=OPTION_COLOR, text_message="RESET", rectangle=reset_surface.get_rect(
        center=(WIDTH // 5.5, HEIGHT // 2 + 298.7)), og_color=BG_COLOR, hover_color=(255, 25, 255))
RESTART_BUTTON = Button(surface=pygame.Surface((reset_text.get_size()[0] + 55, reset_text.get_size()[1] + 55)),
                        fill_color=OPTION_COLOR, text_message="RESTART", rectangle=reset_surface.get_rect(
        center=(WIDTH // 2.1, HEIGHT // 2 + 298.7)), og_color=BG_COLOR, hover_color=(255, 25, 255))
EXIT_BUTTON = Button(surface=pygame.Surface((exit_text.get_size()[0] + 12, exit_text.get_size()[1] + 20)),
                     fill_color=OPTION_COLOR, text_message="EXIT", rectangle=exit_surface.get_rect(
        center=(WIDTH // 1.22, HEIGHT // 2 + 298.7)), og_color=BG_COLOR, hover_color=(255, 25, 255))
END_RESTART_BUTTON = Button(surface=pygame.Surface((reset_text.get_size()[0] + 55, reset_text.get_size()[1] + 30)),
                        fill_color=OPTION_COLOR, text_message="RESTART", rectangle=reset_surface.get_rect(
        center=(WIDTH // 2.1 -5, HEIGHT // 3 + 60)), og_color=BG_COLOR, hover_color=(255, 25, 255))

END_EXIT_BUTTON = Button(surface=pygame.Surface((exit_text.get_size()[0] + 12, exit_text.get_size()[1] + 20)),
                     fill_color=OPTION_COLOR, text_message="EXIT", rectangle=exit_surface.get_rect(
        center=(WIDTH // 2.0 -8, HEIGHT // 3 + 60)), og_color=BG_COLOR, hover_color=(255, 25, 255))

