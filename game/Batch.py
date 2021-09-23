import pygame
from game.objects import Object

font: pygame.font.Font = pygame.font.SysFont(pygame.font.get_default_font(), 25)


def draw_rect(screen, obj: Object):
    pygame.draw.rect(screen, obj.color, (obj.x , obj.y , obj.width, obj.height))


def set_font(font_string, size=25, bold=False, italic=False):
    global font
    font = pygame.font.SysFont(font_string, size, bold, italic)


def draw_text(screen, loc, text, color=(0, 0, 0), background=None):
    global font
    font_surface = font.render(text, True, color, background)
    screen.blit(font_surface, (loc[0], loc[1]-font_surface.get_height()))

