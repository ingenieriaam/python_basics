import pygame
from pygame import mixer
from pathlib import Path  
import os
import random
import math

class Screen():
    def __init__(self, win_width, win_height):
        self.win_width = win_width
        self.win_height = win_height
        #-------------------------------------------------------------
        # create a screen
        self.screen = pygame.display.set_mode((win_width, win_height))
        self.background_src = Path(os.getcwd(),"xtras","fondo.jpg")
        self.background_img = pygame.image.load(self.background_src)
        #-------------------------------------------------------------
        # sounds
        mixer.music.load(Path(os.getcwd(),"xtras","MusicaFondo.mp3"))
        mixer.music.set_volume(0.3)
        mixer.music.play(-1)

        #-------------------------------------------------------------
        # title and icon
        pygame.display.set_caption("space invaders")
        icon_src = Path(os.getcwd(),"xtras","ovni.png")
        icon_img = pygame.image.load(icon_src)
        pygame.display.set_icon(icon_img)

###########################################################
class Player():
    def __init__(self,screen):
        self.src = Path(os.getcwd(),"xtras","cohete.png")
        self.img = pygame.image.load(self.src)
        self.hoffset = self.img.get_height()
        self.woffset = self.img.get_width()
        self.x = (screen.win_width-self.woffset)/2 # middle
        self.y = (screen.win_height-self.hoffset)-20  # bottom
        self.x_change = 0
    #-------------------------------------------------------------
    def set_position(self, screen,x, y):
        """
        The function "player" blits the image of the player onto the screen at the specified coordinates.
        """
        screen.blit(self.img,(x,y))
    #-------------------------------------------------------------
    def set_x_move(self, step):
        self.x_change += step

###########################################################
class Enemy():
    def __init__(self,screen):
        self.move_step = 0.15
        self.src= Path(os.getcwd(),"xtras","enemigo.png")
        self.img= pygame.image.load(self.src)
        self.hoffset= self.img.get_height()
        self.woffset= self.img.get_width()
        self.win_width = screen.win_width
        self.win_height = screen.win_height
        self.x = random.randint(0,self.win_width-self.woffset) 
        self.y = random.randint(50,self.win_height/2)  
        self.x_change = self.move_step  # i want to move the enemy
        self.y_change = self.hoffset/2
        self.lives = True
    #-------------------------------------------------------------
    def ser_move_step(self,step):
        self.move_step = step
    #-------------------------------------------------------------
    def reset(self):
        enemy_x = random.randint(0,self.win_width-self.woffset) 
        enemy_y = random.randint(50,self.win_height-2*self.hoffset)  
        self.x = enemy_x
        self.y = enemy_y
    #-------------------------------------------------------------
    def kill(self):
        self.x = self.win_height*2
        self.y = 0
        self.lives = False
    #-------------------------------------------------------------
    def set_position(self,screen, x, y):
        """
        The function "enemy" blits the image of the enemy onto the screen at the specified coordinates.
        """
        screen.blit(self.img,(x,y))

###########################################################   
class Bullet():
    def __init__(self,screen,player):
        self.src= Path(os.getcwd(),"xtras","bala.png")
        self.img= pygame.image.load(self.src)
        self.hoffset= self.img.get_height()
        self.woffset= self.img.get_width()
        self.win_width = screen.win_width
        self.win_height = screen.win_height
        self.bullet_sound_src = Path(os.getcwd(),"xtras","disparo.mp3")
        self.bang_sound_src = Path(os.getcwd(),"xtras","Golpe.mp3")
        self.x = 0
        self.y = player.x
        self.x_change = 0
        self.y_change = 1
        self.visible = False 
        self.player_ref = player
    #-------------------------------------------------------------
    def sound(self):
        bullet_sound = mixer.Sound(self.bullet_sound_src)
        bullet_sound.play()
    #-------------------------------------------------------------
    def bang_sound(self):
        bullet_sound = mixer.Sound(self.bang_sound_src)
        bullet_sound.play()
    #-------------------------------------------------------------
    def reload(self,player_y):
        self.y = player_y
        self.visible = False
    #-------------------------------------------------------------
    def shoot(self,screen,x, y):
        """
        The function "bullet" blits the image of the bullet onto the screen at the specified coordinates.
        """
        self.visible = True
        screen.blit(self.img,(x + self.player_ref.woffset/2, y + self.player_ref.hoffset/2))
    #-------------------------------------------------------------
    def collision(self,x1,y1,x2,y2):
        dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        if dist < 27: 
            self.visible = False
            return True
        else:
            return False   