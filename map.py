from re import M
import click
import pygame
import map

from block import Block






class Case:

    def __init__(self, x, y, pixelSize) -> None:
        self.x = x
        self.y = y
        self.xPos = x * pixelSize
        self.yPos = y * pixelSize
        self.pixelSize = pixelSize
        self.selected = False
        
    
    def render(self, screen, shiftX, shiftY):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((self.x * self.pixelSize) + shiftX, (self.y * self.pixelSize) + shiftY, self.pixelSize, self.pixelSize))
        xMouse, yMouse = pygame.mouse.get_pos()
        x, y = Map.getXYByXposYpos(self.pixelSize , xMouse, yMouse, shiftX, shiftY)
        if self.selected:
            screen.set_alpha(255)
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((self.x * self.pixelSize) + shiftX, (self.y * self.pixelSize) + shiftY, self.pixelSize, self.pixelSize))
        
        if pygame.mouse.get_pressed()[0]:
            Map.clickMouse0 += 1
            
        for event  in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                Map.clickMouse0 = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    Map.clickMouse0 = 0
                    block = Block.getBlockByXY(x, y)
                    if block != None:
                        Block.remouveBlock(x, y)
        if Map.clickMouse0 == 1:
            print("clicked")
            print(shiftX)
            print("x : " + str(x), " y : " + str(y))
            Map.clickMouse0 += 1
                
            block = Block(x, y, "vert", self.pixelSize)
            
            block2 = Block.getBlockByXY(x, y)
            
            if block2 != None:
                del block
            else:
                block.addToList()
        Block.blocksRender(screen, shiftX, shiftY)

class Map:

    listcase = list()
    
    clickMouse0 = 0

    def __init__(self, sizeX, sizeY, pixelSize) -> None:
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.pixelSize = pixelSize
        x = 0
        y = 0
        while y < sizeY:
            while x < sizeX:
                Map.listcase.append(Case(x, y, self.pixelSize))
                x += 1
            x = 0
            y += 1

    def renderCase(self, screen, shiftX, shiftY):
        for case in Map.listcase:
            case.render(screen, shiftX, shiftY)

    def renderCursor(self, shiftX, shiftY):
        x, y = pygame.mouse.get_pos()
        for case in Map.listcase:
            case.selected = False
            if x > case.xPos + shiftX:
                if x < case.xPos + self.pixelSize + shiftX:
                    if y > case.yPos + shiftY:
                        if y < case.yPos + self.pixelSize + shiftY:
                        
                            case.selected = True
    
    def renderGrid(self, screen, shiftX, shiftY):
        for case in Map.listcase:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((case.x * case.pixelSize) + shiftX, (case.y * case.pixelSize) + shiftY, 2, case.pixelSize))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((case.x * case.pixelSize) + shiftX, (case.y * case.pixelSize) + shiftY, case.pixelSize, 2))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((case.x * case.pixelSize) + shiftX, (case.y * case.pixelSize) + shiftY, -2, case.pixelSize))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((case.x * case.pixelSize) + shiftX, (case.y * case.pixelSize) + shiftY, case.pixelSize, -2))
    
    def getXYByXposYpos(pixelSize, xPos, yPos, shiftX, shiftY):
        return [int((xPos - shiftX) / pixelSize), int((yPos - shiftY) / pixelSize)]
                            
