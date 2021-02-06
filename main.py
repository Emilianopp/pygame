
"""
Author Emiliano Penaloza
Small game I made for my sister's birthday
Space invader like clone
"""

import pygame
from enemy import enemy
from sister import sister
from laser import laser


pygame.init()

#Enemy
emis = []
coord = 64

"""
Primative attempt at setting the enemy's coordanates on the grid
Decided to draw an inverted pascals triangle with the highest order being seven
This portion of the code should have been implemented how I implment the use of lasers later
"""
for i in range(0, 16):
    emis.append(enemy())
for i in range(0, 16):
    if (i < 7):
        emis[i].setcoords(x=coord, y=32)
        coord += 64 + 32
    if (7 <= i) & (i < 12):
        if (i == 7):
            coord = 160
        emis[i].setcoords(x=coord, y=32 * 3)
        coord += 64 + 32
    if (12 <= i) & (i < 15):
        if (i == 12):
            coord = 256
        emis[i].setcoords(x=coord, y=32 * 5)
        coord += 64 + 32
    if (i == 15):
        coord = 352
        emis[i].setcoords(x=coord, y=32 * 7)

width = 800
height = 600
screen = pygame.display.set_mode((width,height), )
pygame.display.set_caption("Emiliano Space Invader ")

"""
Player variables 
initiate a sister object as my sisters name 
"""
#Player
sisterX = width/2 - 32
sisterY = height - 64*2
movement = 0
natalia = sister(sisterX,sisterY)

#laser
"""
Initiating laser objects
elote means corn in spanish which is my sisters favourite food
el is short for elephant which is what the enemy(me) are shooting 
"""
elote = []
el = []


"""
In retrospect this should have been a single intersect function and a figure class should have been implemented
This figure class would work as a parent class for each of the other classes meaning only one intersect function would have been necesary 
"""
#intersect function
def laserIntersect(elote = laser, phant  = laser):
    if( phant.getY() < elote.getY() + 16) & (elote.getY() < phant.getY()):
        if(elote.getX() > phant.getX()) * (elote.getX() < phant.getX() + 32):
            return True
        elif(elote.getX() +32 > phant.getX()) & (elote.getX() + 32 < phant.getX() +32):
            return True



def intersectSister(elote  = laser, natalia  = sister):
    if(elote.y < natalia.getY() + 64 ) & (elote.y > natalia.getY()):
        if(elote.x > natalia.getX()) & (elote.x < natalia.getX()+ 64):
            return True

        elif(elote.x + 32 > natalia.getX()) & (elote.x + 32 < natalia.getX() + 64):
            return True
def intersect(elote  = laser, emi  = enemy):
    if(elote.y < emi.y_cord + 64 ) & (elote.y > emi.y_cord):
        if(elote.x > emi.x_cord) & (elote.x < emi.x_cord + 64):
            return True

        elif(elote.x + 32 > emi.x_cord) & (elote.x + 32 < emi.x_cord + 64):
            return True




#Updator function
"""
Initiating some variable objects that will be used in the while loop 
as well as background images
"""
running = True
test = True
timer = 601
timer2 = 1001
count = 0
change = 5
enemy_count = 0
win = False
background  = pygame.transform.scale(pygame.image.load('background.jpg'), (800, 600))
over = pygame.transform.scale(pygame.image.load('press_a.jpg'), (800, 600))
winner = pygame.transform.scale(pygame.image.load('pressA.jpg'), (800, 600))

"""
game loop running is a variable to see if either the player has won or lost 
if running is set to false the next two while loops check if player has won or if it has lost 
if player has won it loads the winner screen 
likewise, if player has lost it loads game over screen 
game can be re-started in both cases by pressing key a
"""
while running:
    while running:
        j = 3
        bool = False
        screen.blit(background,(0,0))

        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN :
                if (event.key == pygame.K_LEFT) :
                    movement = -2
                elif (event.key == pygame.K_RIGHT):
                        movement = 2
                if event.key  == pygame.K_SPACE:
                    bool = True
                if event.key == pygame.K_SPACE:
                    if timer > 600:
                        timer = 0
                        elote.append(laser(natalia.sisterMidX(),natalia.sisterMidY()))
            elif(event.type == pygame.KEYUP):
                if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                    movement = 0
        count = 0
        for e in emis:
            if(e != None):
                screen.blit(e.getEmi(),(e.getX(),e.getY()))
                if(timer2 > 1000) & (emis.index(e)%2 == 0):
                    el.append(laser(e.getX()+ 16,e.getY() + 32))
                elif(timer2 == 500) & emis.index(e)%2 != 0:
                    el.append(laser(e.getX() + 16, e.getY() + 32))
            elif(e == None):
                count += 1

            if(count == len(emis)):
                running = False
                win = True


        if(timer2 <= 1000):
            timer2 += 1
        else:
            timer2 = 0

        for k in el:
            if(k.getY() > 0):
                if (k != None):
                    for m in elote:
                        if (laserIntersect(m, k)):
                            el.remove(k)
                            elote.remove(m)
                    screen.blit(k.getPhant(),(k.getX(),k.getY()))
                    k.y += .5
                    if(intersectSister(k,natalia)):
                        running = False
            else:
                el.remove(k)

        for m in elote:
            if(m.getY() > 0):
                screen.blit(m.getElote(), (m.getX(), m.getY()))
                m.y += -1
                timer+= 5
                for e in range(0 , len(emis)):
                 if(emis[e] == None):
                     pass
                 elif(intersect(m,emis[e])):
                    elote.remove(m)
                    emis[e] = None

        natalia.changeSister(movement)
        screen.blit(natalia.getNatalia(), (natalia.getX(),natalia.getY()))
        pygame.display.update()

    while (running == False) & (win == False):
        pygame.display.flip()
        screen.blit(over,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_a):
                    running = True
                    pygame.display.flip()
                    timer = 601
                    timer2 = 1001
                    count = 0
                    change = 5
                    enemy_count = 0
                    emis = []
                    elote = []
                    el = []
                    coord = 64
                    for i in range(0, 16):
                        emis.append(enemy())
                    for i in range(0, 16):
                        if (i < 7):
                            emis[i].setcoords(x=coord, y=32)
                            coord += 64 + 32
                        if (7 <= i) & (i < 12):
                            if (i == 7):
                                coord = 160
                            emis[i].setcoords(x=coord, y=32 * 3)
                            coord += 64 + 32
                        if (12 <= i) & (i < 15):
                            if (i == 12):
                                coord = 256
                            emis[i].setcoords(x=coord, y=32 * 5)
                            coord += 64 + 32
                        if (i == 15):
                            coord = 352
                            emis[i].setcoords(x=coord, y=32 * 7)

    while (running == False) & (win == True):
        pygame.display.flip()
        screen.blit(winner,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_a):
                    running = True
                    win = False
                    pygame.display.flip()
                    timer = 601
                    timer2 = 1001
                    count = 0
                    change = 5
                    enemy_count = 0
                    emis = []
                    elote = []
                    el = []
                    coord = 64
                    for i in range(0, 16):
                        emis.append(enemy())
                    for i in range(0, 16):
                        if (i < 7):
                            emis[i].setcoords(x=coord, y=32)
                            coord += 64 + 32
                        if (7 <= i) & (i < 12):
                            if (i == 7):
                                coord = 160
                            emis[i].setcoords(x=coord, y=32 * 3)
                            coord += 64 + 32
                        if (12 <= i) & (i < 15):
                            if (i == 12):
                                coord = 256
                            emis[i].setcoords(x=coord, y=32 * 5)
                            coord += 64 + 32
                        if (i == 15):
                            coord = 352
                            emis[i].setcoords(x=coord, y=32 * 7)

"""
Overall code should be cleaned up, a lot of the code should have been implemented with use of functions 
Figure class should have been implemented 
Implementation of enemy class was incorrect 
Overall proud of small project much to improve on
"""
