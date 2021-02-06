import pygame
class sister:
    natalia = pygame.transform.scale(pygame.image.load('nataliabird1.png'),(64,64))
    changeSister = 0
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x  = x
        self.y  = y
    def changeSister(self,change):
        tmp = self.x + change
        if(tmp < 800-64) & (0 < tmp):
            self.x = tmp
        else:
            pass
    def sisterMidX(self):
        return self.x + 16
    def sisterMidY(self):
        return self.y + 32
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNatalia(self):
        return self.natalia

