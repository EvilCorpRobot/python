
from math import pi
from uuid import UUID, uuid4

import pygame




class Block:

    blocksList = list()

    def __init__(self, x, y, type, pixelSize):
        self.x = x
        self.y = y
        self.type = type
        self.pixelSize = pixelSize
        self.uuid = uuid4()
        self.vert = (0, 255, 0)

    def addToList(self):
        Block.blocksList.append(self)
    
    def getBlockByUUID(uuid):
        for block in Block.blocksList:
            if uuid == block.uuid:
                return block
        return None

    def getBlockByXY(x, y):
        
        for block in Block.blocksList:
            if int(x) == block.x:
                if int(y) == block.y:
                    return block
        return None

    def remouveBlock(x, y):
        for blocks in Block.blocksList:
            if x == blocks.x:
                if y == blocks.y:
                    Block.blocksList.remove(blocks)
                    del blocks
    
    def blocksRender(screen, shiftX, shiftY):
        for block in Block.blocksList:
            block.render(screen, shiftX, shiftY)


    def render(self, screen, shiftX, shiftY):
        screen.set_alpha(255)
        pygame.draw.rect(screen, self.vert, pygame.Rect((self.x * self.pixelSize) + shiftX, (self.y * self.pixelSize) + shiftY, self.pixelSize, self.pixelSize))
