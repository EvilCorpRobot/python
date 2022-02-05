import sys
import pygame
import python.map as map
def render():
    pass

def update():
    pass

pygame.init()
size = (1080, 720)
black = (0, 0, 0)
map1 = map.Map(9, 10, 50)
screen = pygame.display.set_mode(size, pygame.SRCALPHA)
shiftX = 0
shiftY = 0
while 1:
    screen.fill(black)
    rel =  pygame.mouse.get_rel()
    if pygame.mouse.get_pressed()[1]:
        if not rel[0] < 1:
            shiftX += rel[0]
        if not rel[0] > 1:
            shiftX += rel[0]
        if not rel[1] < 1:
            shiftY += rel[1]
        if not rel[1] > 1:
            shiftY += rel[1]
    map1.renderCase(screen, shiftX, shiftY)
    map1.renderCursor(shiftX, shiftY)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
