import math
import pygame
class buildEnvironment:
    def __init__(self,MapDimensions):
        pygame.init()
        self.pointCloud = []
        self.externalMap = pygame.image.load('floor_plan.png')
        self.maph, self.mapw = MapDimensions
        self.MapwindowName = 'RRT Path Planning'
        pygame.display.set_caption(self.MapwindowName)
        self.map = pygame.display.set_mode(self.mapw,self.maph)
        self.map.blit(self.externalMap,(0,0))
        ## Commonly used Colors
        self.black = (0, 0, 0)
        self.grey = (70, 70, 70)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)

