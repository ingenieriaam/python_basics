import pygame

pygame.init()

height = 480
width = 640

screen = pygame.display.set_mode((width, height))

execute = True

while execute:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execute = False
