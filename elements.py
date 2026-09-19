import time
import random

class slider:

    def __init__(self,y,t_time,screen,pygame,h = 20,l = 300):
        self.fixed_time = t_time
        self.time = t_time
        self.last_time = time.time()
        self.h = h
        self.r_l = l
        self.l = (self.time * (self.r_l/self.fixed_time))
        self.x = screen.get_width()/2 - self.l/2
        self.y = y
        self.screen = screen
        self.pyg = pygame

    def update(self):
        if self.time >= 0:
            self.pyg.draw.rect(self.screen,(0,20,255),(self.x,self.y,self.l,self.h))
            self.last_time = time.time()
            self.time = self.time - ((time.time() - self.last_time) * 1000)
            self.h = 30
            self.l = (self.time * (self.r_l/self.fixed_time))
            self.x = self.screen.get_width()/2 - self.l/2
        else:
            return("haha")

def imposter_color(rgb, d):
    for _ in range(100):
        new = tuple(max(0, min(255, c + random.randint(-d, d))) for c in rgb)
        if sum(abs(a - b) for a, b in zip(rgb, new)) >= d:
            return new
    return tuple(max(0, min(255, c + d if c < 128 else c - d)) for c in rgb)

class rect:
    def __init__(self,e,rgb,d,imposter,pygame,screen):
        self.e = e
        self.d = d
        self.imposter = imposter
        self.rgb = imposter_color(rgb,d) if self.imposter == self.e else rgb

        self.pygame = pygame
        self.screen = screen
        self.l = (screen.get_width()-30)/3 - 10
        self.h = screen.get_height() - 150
        if self.e == 1:
            self.x = self.l * 0+ 20
        elif self.e == 2:
            self.x = self.l * 1 + 30
        elif self.e == 3:
            self.x = self.l * 2 + 40
        self.y = 100


    def update(self,event):
        if event == self.e:
            self.pygame.draw.rect(self.screen,(80,80,200),(self.x-5,self.y-5,self.l+10,self.h+10))
        self.pygame.draw.rect(self.screen,self.rgb,(self.x,self.y,self.l,self.h))

