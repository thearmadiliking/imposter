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

class rect:
    def __init__(self,e,rgb,d,imposter,pygame,screen):
        self.e = e
        self.d = d
        trys = 0
        self.rgb = rgb if imposter != e else (max(min(rgb[0]+random.randint(-self.d,self.d),255),0), max(min(rgb[1]+random.randint(-self.d,self.d),255),0), max(min(rgb[2]+random.randint(-self.d,self.d),255),0))
        while (rgb[0] - self.rgb[0]) + (rgb[1] - self.rgb[1]) + (rgb[2] - self.rgb[2]) <= d-5 and imposter == e:
            print(f"try {trys}")
            trys += 1
            self.rgb = (max(min(rgb[0]+random.randint(-self.d,self.d),255),0), max(min(rgb[1]+random.randint(-self.d,self.d),255),0), max(min(rgb[2]+random.randint(-self.d,self.d),255),0))
        print(f"final rgb: {self.rgb}")
        self.imposter = imposter
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


    def update(self):
        self.pygame.draw.rect(self.screen,self.rgb,(self.x,self.y,self.l,self.h))

