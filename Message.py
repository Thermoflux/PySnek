"""
Message.
Prints messages to show to the user.
Author: Thermoflux

"""
import pygame
# Message class
class Message(object):
    """ Class used to display text in game window"""
    # -- Methods
    # Constructor
    def __init__(self, text, x, y, screen, color):
        self.font = pygame.font.SysFont("serif", 25)
        self.text = self.font.render(text, True, color)
        screen.blit(self.text, [x, y])
