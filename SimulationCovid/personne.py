import pygame
from random import *
from math import sqrt

white = [255, 255, 255]
black = [0, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]
grey = [105, 105, 105, 105]

pygame.init()


class Humain:

    nbr_humains_max = 100
    nbr_humains = 0

    contamines = dict()
    soigne = dict()
    time_infection = dict()

    humains = dict()
    normal = dict()
    infecte = dict()

    def __init__(self):
        self.UUID  = Humain.nbr_humains + 1
        Humain.nbr_humains += 1
        Humain.contamines[self.UUID] = False
        Humain.soigne[self.UUID] = False
        Humain.time_infection[self.UUID] = 0

    def move():
        for h in Humain.humains.values():
            if h.x < 20 or h.x > 1060:
                h.vx *= -1
            if h.y < 20 or h.y > 700:
                h.vy *= -1
            h.x += 0.2 * h.vx
            h.y += 0.2 * h.vy

    def checkInfected():
        for k in Humain.humains.keys():
            h = Humain.humains[k]
            for c in Humain.contamines.keys():
                if Humain.contamines[c] == True and Humain.soigne[k] == False:
                    i = Humain.humains[c]
                    dist = sqrt((h.x - i.x)**2 + (h.y - i.y)**2)
                    if dist <= 25:
                        Humain.contamines[k] = True
   

    def getUuid(self):
        return self.UUID
    def getNbrHumains(self):
        return Humain.nbr_humains
    def getNbrHumainsMax(self):
        return Humain.nbr_humains_max
    def getHumains(nbr):
        return Humain.humains[str(nbr)]
    def printlist():
        print(humains)


class Normal(Humain):
    nbr_normals = 0

    def __init__(self):
        Humain.__init__(self)
        self.x = randint(20, 1060)
        self.y = randint(20, 700)
        self.vx = choice([-1.00, 1.00])
        self.vy = choice([-1.00, 1.00])
        Normal.nbr_normals += 1
        Humain.humains[self.getUuid()] = self
        Humain.contamines[self.getUuid()] = False
    
    
    def getPOSX(self):
        return self.x
    def getPOSY(self):
        return self.y
    def getSurface(self):
        return self.surface

class Infecte(Humain):
    nbr_infecte = 0

    def __init__(self):
        Humain.__init__(self)
        self.x = randint(20, 1060)
        self.y = randint(20, 700)
        self.vx = choice([-1.00, 1.00])
        self.vy = choice([-1.00, 1.00])
        Humain.humains[self.getUuid()] = self
        Humain.infecte[self.getUuid()] = self
        Humain.contamines[self.getUuid()] = True
        Infecte.nbr_infecte += 1

    
    def getPOSX(self):
        return self.x
    def getPOSY(self):
        return self.y
    def getSurface(self):
        return self.surface

def show(screen, normal, infecte):
    for humains in Humain.contamines.keys():
        if Humain.soigne[humains] == True:
            h = Humain.humains[humains]
            print(1)
            pygame.draw.circle(screen , grey, [h.getPOSX(), h.getPOSY()], 10)
            pygame.display.flip()
            break
        if Humain.contamines[humains] == False:
            h = Humain.humains[humains]
            pygame.draw.circle(screen , blue, [h.getPOSX(), h.getPOSY()], 10)

        elif Humain.contamines[humains] == True:
            h = Humain.humains[humains]
            pts = Humain.time_infection[humains]
            Humain.time_infection[humains] = pts + 1
            print(Humain.time_infection[humains])
            pygame.draw.circle(screen , green, [h.getPOSX(), h.getPOSY()], 10)
        if Humain.time_infection[humains] > 1000:
                print("1")
                Humain.soigne[humains] = True
                pygame.display.flip()
                break
    pygame.display.flip()




    
class Fenetre:

    def __init__(self):
        pygame.display.set_caption("Simulation Maladie")
        screen = pygame.display.set_mode((1080, 720))
        screen.fill(white)
        pygame.display.flip()
        run = True
        nbr_max = Humain.nbr_humains_max
        print(nbr_max)
        for humainNormal in range(1,nbr_max + 1):
            humainNormal = Normal()
            pygame.draw.circle(screen , blue, [humainNormal.getPOSX(), humainNormal.getPOSY()], 5)
            pygame.display.flip()
        humai1_infecte = Infecte()
        pygame.draw.circle(screen, green, [humai1_infecte.getPOSX(), humai1_infecte.getPOSY()], 5)
        pygame.display.flip()
        print(Humain.soigne)
        while run:
            Humain.move()
            Humain.checkInfected()
            show(screen, Humain.normal, Humain.infecte)
            pygame.display.update()
            screen.fill(white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
    
    


start = Fenetre()