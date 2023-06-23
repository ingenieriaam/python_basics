import pygame
from pygame import mixer
from pathlib import Path  
import os
import random
import math
###########################################################
# init pygame
pygame.init()

win_height = 480
win_width = 640
MOVE_STEP = 0.3
score=0
###########################################################
# create a screen
screen = pygame.display.set_mode((win_width, win_height))
background_src = Path(os.getcwd(),"xtras","fondo.jpg")
background_img = pygame.image.load(background_src)
font = pygame.font.Font('freesansbold.ttf', 32)
score_x = 10
score_y = 10

###########################################################
# sounds
bullet_sound_src = Path(os.getcwd(),"xtras","disparo.mp3")
bang_sound_src = Path(os.getcwd(),"xtras","Golpe.mp3")
Path(os.getcwd(),"xtras","Golpe.mp3")
mixer.music.load(Path(os.getcwd(),"xtras","MusicaFondo.mp3"))
mixer.music.set_volume(0.3)
mixer.music.play(-1)

###########################################################
# title and icon
pygame.display.set_caption("space invaders")
icon_src = Path(os.getcwd(),"xtras","ovni.png")
icon_img = pygame.image.load(icon_src)
pygame.display.set_icon(icon_img)

###########################################################
# player image
player_src = Path(os.getcwd(),"xtras","cohete.png")
player_img = pygame.image.load(player_src)
player_hoffset = player_img.get_height()
player_woffset = player_img.get_width()
player_x = (win_width-player_woffset)/2 # middle
player_y = (win_height-player_hoffset)-20  # bottom
player_x_change = 0

def player(x, y):
    """
    The function "player" blits the image of the player onto the screen at the specified coordinates.
    """
    screen.blit(player_img,(x,y))
###########################################################
# ENEMY image
enemies = 8

enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_Y_change = []

enemy_src= Path(os.getcwd(),"xtras","enemigo.png")
enemy_img= pygame.image.load(enemy_src)
enemy_hoffset= enemy_img.get_height()
enemy_woffset= enemy_img.get_width()

for e in range(enemies):
    enemy_x.append(random.randint(0,win_width-enemy_woffset) )
    enemy_y.append(random.randint(50,win_height-player_hoffset-enemy_hoffset)  )
    enemy_x_change.append(MOVE_STEP)# i want to move the enemy
    enemy_Y_change.append(enemy_hoffset/2)

def enemy_reset():
    enemy_x = random.randint(0,win_width-enemy_woffset) 
    enemy_y = random.randint(50,win_height-player_hoffset-enemy_hoffset)  
    return enemy_x, enemy_y
def enemy(x, y):
    """
    The function "enemy" blits the image of the enemy onto the screen at the specified coordinates.
    """
    screen.blit(enemy_img,(x,y))
###########################################################
# bullet image
bullet_src = Path(os.getcwd(),"xtras","bala.png")
bullet_img = pygame.image.load(bullet_src)
bullet_hoffset = bullet_img.get_height()
bullet_woffset = bullet_img.get_width()
bullet_x = 0
bullet_y = player_y
bullet_x_change = 0 
bullet_Y_change = 1
bullet_visible = False 

def shoot_bullet(x, y):
    """
    The function "bullet" blits the image of the bullet onto the screen at the specified coordinates.
    """
    global bullet_visible
    bullet_visible = True
    screen.blit(bullet_img,(x + player_woffset/2, y + player_hoffset/2))

###########################################################

def collision(x1,y1,x2,y2):
    global bullet_visible
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if dist < 27: 
        bullet_visible = False
        return True
    else:
        return False    

def show_score(x, y):
    """
    The function "show_score" blits the score onto the screen at the specified coordinates.
    """
    global score
    score_text = font.render("Score: "+str(score),True,(255,255,255))
    screen.blit(score_text,(x,y))

def final_text():
    final = font.render("GAME OVER",True,(255,255,255))
    screen.blit(final,(200,60))

###########################################################
# GAME LOOP
###########################################################
execute = True
while execute:
    # get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execute = False
        # press key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change -= MOVE_STEP
            if event.key == pygame.K_RIGHT:
                player_x_change += MOVE_STEP
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound(bullet_sound_src)
                bullet_sound.play()
                if not bullet_visible:
                    bullet_x = player_x
                    shoot_bullet(bullet_x, bullet_y)
        # release key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    #--------------------------------
    # paint the screen        
    screen.blit(background_img,(0,0))

    #--------------------------------
    # move player 
    player_x += player_x_change
    # on ranges check
    if player_x <= 0:
        player_x = 0
    elif player_x >= win_width - player_woffset:
        player_x = win_width - player_woffset

    player(player_x, player_y)
    #--------------------------------
    # move enemies
    for e in range(enemies): 
        # end of gane
        if enemy_y[e] >= win_height-2*player_hoffset:
            for k in range(enemies):
                enemy_y[k] = win_height*2 # not visible
            final_text()
            break

        enemy_x[e] += enemy_x_change[e]
        # on ranges check
        if enemy_x[e] <= 0:
            enemy_x_change[e] = 0.3 # i want to move the enemy when it reaches the side
            enemy_y[e] += enemy_Y_change[e]
        elif enemy_x[e] >= win_width - enemy_woffset:
            enemy_x_change[e] = -0.3
            enemy_y[e] += enemy_Y_change[e]
        #--------------------------------
        coll = collision(enemy_x[e], enemy_y[e], bullet_x, bullet_y)
        if coll:
            bullet_y = player_y
            bullet_visible = False
            score += 1
            enemy_x[e], enemy_y[e] = enemy_reset()
            bang_sound = mixer.Sound(bang_sound_src)
            bang_sound.play()
        enemy(enemy_x[e], enemy_y[e])
    
    #--------------------------------
    # Move bullet
    # reload
    if bullet_y <= bullet_hoffset:
        bullet_y = player_y
        bullet_visible = False
    # shoot
    if bullet_visible: 
        shoot_bullet(bullet_x - player_woffset/4, bullet_y)
        bullet_y -= bullet_Y_change
    
    #--------------------------------
    show_score(score_x, score_y)
    pygame.display.update()
    
