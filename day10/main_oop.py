import pygame
from pygame import mixer
from pathlib import Path  
import os
import random
import math
import gamecomponents as gc
###########################################################
# init pygame
pygame.init()

win_height = 480
win_width = 640
MOVE_STEP = 0.3
score=0
score_x = 10
score_y = 10
font = pygame.font.Font('freesansbold.ttf', 32)

###########################################################
# create a screen
myScreen = gc.Screen(win_width, win_height)
###########################################################
# player object
player1 = gc.Player(myScreen)
###########################################################
# ENEMIES objects
enemiesNum = 8
enemies = []
for e in range(enemiesNum):
    enemies.append( gc.Enemy(myScreen) )

###########################################################
# bullet object
bullet = gc.Bullet(myScreen,player1)

###########################################################
def show_score(x, y):
    """
    The function "show_score" blits the score onto the screen at the specified coordinates.
    """
    global score
    score_text = font.render("Score: "+str(score),True,(255,255,255))
    myScreen.screen.blit(score_text,(x,y))

def final_text():
    final = font.render("GAME OVER",True,(255,255,255))
    myScreen.screen.blit(final,(200,60))

###########################################################
# GAME LOOP
###########################################################

execute = True
while execute:
    # get events
    for event in pygame.event.get():
        quit_button    = (event.type == pygame.QUIT)
        press_button   = (event.type == pygame.KEYDOWN)
        left_button    = (event.type == pygame.K_LEFT)
        right_button   = (event.type == pygame.K_RIGHT)
        space_button   = (event.type == pygame.K_SPACE)
        release_button = (event.type == pygame.KEYUP)

        if quit_button:
            execute = False

        if press_button:
            if left_button:
                player1.set_x_change(MOVE_STEP)
            if right_button:
                player1.set_x_change(MOVE_STEP)
            if space_button:
                bullet.sound()
                if not bullet.visible:
                    bullet.x = player1.x
                    bullet.shoot(myScreen.screen,bullet.x, bullet.y)

        if release_button:
            if left_button or right_button:
                player1.set_x_change(0)
    #--------------------------------
    # paint the screen        
    myScreen.screen.blit(myScreen.background_img,(0,0))

    #--------------------------------
    # move player 
    player1.x += player1.x_change
    # on ranges check
    if player1.x <= 0:
        player1.x = 0
    elif player1.x >= win_width - player1.woffset:
        player1.x = win_width - player1.woffset

    player1.set_position(myScreen.screen,player1.x, player1.y)
    #--------------------------------
    # move enemies
    for e in range(enemiesNum): 
        # end of gane
        if enemies[e].y >= win_height-2*player1.hoffset:
            for k in range(enemiesNum):
                enemies[k].y = win_height*2 # not visible
            final_text()
            break

        enemies[e].x += enemies[e].x_change
        # on ranges check
        if enemies[e].x <= 0:
            enemies[e].x_change = 0.3 # i want to move the enemies when it reaches the side
            enemies[e].y += enemies[e].y_change
        elif enemies[e].x >= myScreen.win_width - enemies[e].woffset:
            enemies[e] .x_change = -0.3
            enemies[e].y += enemies[e].y_change
        #--------------------------------
        coll = bullet.collision(enemies[e].x, enemies[e].y, bullet.x, bullet.y)
        if coll:
            bullet.reload(player1.y)
            score += 1
            enemies[e].reset()
            bullet.bang_sound()
        enemies[e].set_position(myScreen.screen,enemies[e].x, enemies[e].y)
    
    #--------------------------------
    # Move bullet
    # reload
    if bullet.y <= bullet.hoffset:
        bullet.reload(player1.y)
    # shoot
    if bullet.visible: 
        bullet.shoot(myScreen.screen,bullet.x - player1.woffset/4, bullet.y)
        bullet.y -= bullet.y_change
    
    #--------------------------------
    show_score(score_x, score_y)
    pygame.display.update()
    
