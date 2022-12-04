from constants import *
import pygame
pygame.init()
user_font = pygame.font.Font(None, USERADD_FONT)
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
    def get_value(self):
        return self.value
    def get_pos(self):
        return self.pos

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        if self.value == 0:
            number_surf = user_font.render("", 0, ADDED_COLOR)
        else:
            number_surf = user_font.render(str(self.value), 0, ADDED_COLOR)
        number_rect = number_surf.get_rect(
            center=(CHIP_SIZE * self.col + CHIP_SIZE // 2, CHIP_SIZE * self.row + CHIP_SIZE // 2))
        self.screen.blit(number_surf, number_rect)
