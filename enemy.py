import pygame

class enemy:
    y_cord = 0
    x_cord = 0
    intersect = False
    emi = pygame.transform.scale(pygame.image.load("emi.png"), (64, 64))
    def getX(self):
        return self.x_cord
    def getY(self):
        return self.y_cord
    def xset(self,x):
        self.x_cord = x
    def getEmi(self):
        return self.emi
    def xset(self, y):
        self.y_cord = y
    def setcoords(self,x,y):
        self.y_cord = y
        self.x_cord = x





