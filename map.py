import pygame
class Case:

    def __init__(self, x, y, pixelSize) -> None:
        self.x = x
        self.y = y
        self.xPos = x * pixelSize
        self.yPos = y * pixelSize
        self.pixelSize = pixelSize
        self.selected = False
    
    def render(self, screen, shiftX, shiftY):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((self.x * self.pixelSize) + shiftX, (self.y * self.pixelSize) + shiftY, 60, 60))
        if self.selected:
            screen.set_alpha(255)
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((self.x * self.pixelSize) + shiftX, (self.y * self.pixelSize) + shiftY, 60, 60))

class Map:

    listcase = list()

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
