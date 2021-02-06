import pygame
class laser:
    elote = pygame.transform.scale(pygame.image.load('elote.png'), (32, 16))
    phant  = pygame.transform.scale(pygame.image.load('ele.jpg'), (32, 16))
    speed = 5
    x = 0
    y = 0
    intersect = False

    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getPhant(self):
        return self.phant
    def getElote(self):
        return self.elote
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getSpeed(self):
        return self.speed
    def setX(self,x):
        self.x = x

    def setY(self, y):
        self.y = y
    def setCoord(self,x,y):
        self.x = x
        self.y = y

    def fired(self,bool):
        if(bool):
            while (self.x < 600) & self.intersect == False:
                self.x += self.speed

