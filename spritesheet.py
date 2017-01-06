"""
This module is used to pull individual sprites from sprite sheets.
"""
import pygame


class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """
    # This points to our sprite sheet image
    sprite_sheet = None

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, WIDTH, HEIGHT):
        # Create a new blank image
        image = pygame.Surface([WIDTH, HEIGHT]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, WIDTH, HEIGHT))

        # Return the image
        return image
