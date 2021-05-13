import pygame
from random import *
from math import sqrt
import time


white = [255, 255, 255]
black = [0, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]
grey = [105, 105, 105, 105]

pygame.init()

tailles_cercle = 7

size_conf = 80


class Humain:
    nbr_humains_max = 200
    nbr_humains = 0
    #etats = 0 : Non infécté, 1 : infecté, 2 guérie
    humain_etat = dict()
    humain_uuid = dict()

    def __init__(self):
        pass
    
    def createSimulation(self):
        for h in range(1, Humain.nbr_humains_max):
            p = Normal()
            pygame.draw.circle(screen , blue, [p.getPOSX(), p.getPOSY()], 10)
            pygame.display.flip()
        h_inf = Infecte(x=randint(20, 1060), y=randint(20, 700), vx=choice([-1.00, 1.00]), vy=choice([-1.00, 1.00]))
        pygame.draw.circle(screen, green, [h_inf.getPOSX(), h_inf.getPOSY()], 10)
        pygame.display.flip()
    
    def move(self):
        for k in Humain.humain_uuid.keys():
            h = Humain.humain_uuid[k]
            if h.x < 20 or h.x > 1060:
                h.vx *= -1
            if h.y < 20 or h.y > 700:
                h.vy *= -1
            h.x += 2.5 * h.vx
            h.y += 2.5 * h.vy

    def moveConfinement(self):
        for k in Humain.humain_uuid.keys():
            h = Humain.humain_uuid[k]
            if h.x < h.getConfx() - size_conf or h.x > h.getConfx() + size_conf:
                h.vx *= -1
            if h.y < h.getConfy() - size_conf or h.y > h.getConfy() + size_conf:
                h.vy *= -1
            h.x += 2.5 * h.vx
            h.y += 2.5 * h.vy

    
    def checkInfected(self):
        uuid = Humain.humain_uuid.copy()
        for k in uuid.keys():
            h = Humain.humain_uuid[k]
            try: 
                if h.time_infection > 150:
                    h.soigne()
                break
            except:
                pass
            if Humain.humain_etat[k] == False:
                a = Humain.humain_etat.copy()
                for ck in a.keys():
                    i = Humain.humain_uuid[ck]
                    et = a[ck]
                    if et == 1:
                        dist = sqrt((h.getPOSX() - i.getPOSX())**2 + (h.getPOSY() - i.getPOSY())**2)
                        if dist <= 25:
                            h.infected()

    def getConfx(self):
        return int(self.confx)
    def getConfy(self):
        return int(self.confy)
    

    
    def show(self):  
        pygame.display.update()
        screen.fill(white)
        for key in Humain.humain_uuid.keys():
            value = Humain.humain_etat[key]
            if Humain.humain_etat[key] == False:
                h = Humain.humain_uuid[key]
                pygame.draw.circle(screen , blue, [h.getPOSX(), h.getPOSY()], tailles_cercle)
            elif Humain.humain_etat[key] == 1:
                h = Humain.humain_uuid[key]
                h.time_infection += 1
                pygame.draw.circle(screen , green, [h.getPOSX(), h.getPOSY()], tailles_cercle)
            elif Humain.humain_etat[key] == 2:
                h = Humain.humain_uuid[key]
                pygame.draw.circle(screen , grey, [h.getPOSX(), h.getPOSY()], tailles_cercle)
        pygame.display.flip()
            
    def getUuid(self):
        return self.UUID


class Normal(Humain):

    def __init__(self):
        super().__init__()
        self.UUID  = Humain.nbr_humains + 1
        self.x = int(randint(20, 1060))
        self.y = int(randint(20, 700))
        self.vx = choice([-1.00, 1.00])
        self.vy = choice([-1.00, 1.00])
        self.confx = self.x 
        self.confy = self.x
        Humain.humain_uuid[self.getUuid()] = self
        Humain.humain_etat[self.getUuid()] = False
        Humain.nbr_humains += 1
    
    def getPOSX(self):
        return self.x
    def getPOSY(self):
        return self.y
    def getVX(self):
        return self.vx
    def getVY(self):
        return self.vy
    def infected(self):
        try:
            del Humain.humain_uuid[self.getUuid()]
            del Humain.humain_etat[self.getUuid()]
        except:
            pass
        finally:
            inf = Infecte(self.x, self.y, self.vx, self.vy)
    
class Infecte(Humain):

    def __init__(self, x, y, vx, vy):
        super().__init__()
        self.UUID  = Humain.nbr_humains + 1
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.confx = self.x 
        self.confy = self.x
        self.time_infection = 0
        Humain.humain_uuid[self.getUuid()] = self
        Humain.humain_etat[self.getUuid()] = 1
        Humain.nbr_humains += 1
        
    
    def getPOSX(self):
        return self.x
    def getPOSY(self):
        return self.y
    def getVX(self):
        return self.vx
    def getVY(self):
        return self.vy
    
    def soigne(self):
        try:   
            del Humain.humain_uuid[self.getUuid()]
            del Humain.humain_etat[self.getUuid()]
        except:
            pass
        finally:
            gue = Guerie(self.x, self.y, self.vx, self.vy)

class Guerie(Humain):

    def __init__(self, x, y, vx, vy):
        super().__init__()
        self.UUID  = Humain.nbr_humains + 1
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.confx = self.x 
        self.confy = self.x
        Humain.humain_uuid[self.getUuid()] = self
        Humain.humain_etat[self.getUuid()] = 2
        Humain.nbr_humains += 1
    
    def getPOSX(self):
        return self.x
    def getPOSY(self):
        return self.y
    def getVX(self):
        return self.vx
    def getVY(self):
        return self.vy
    

pygame.display.set_caption("Simulation Maladie")
screen = pygame.display.set_mode((1080, 720))
screen.fill(white)
pygame.display.flip()

sim = Humain()
sim.createSimulation()
run = True
while run:
    sim.moveConfinement()
    sim.checkInfected()
    sim.show()
    time.sleep(0.04)
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
