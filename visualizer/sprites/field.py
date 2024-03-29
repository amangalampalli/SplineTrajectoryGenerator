import pygame

from visualizer.utilities.utils import load_image


class Field(pygame.sprite.Sprite):
    def __init__(self, screen, location=[0, 0]):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = load_image(144, '/home/tinku/SplineTrajectoryGenerator/visualizer/assets/Field.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.screen = screen.get_rect()
