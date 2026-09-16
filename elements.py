import time

class slider:

    def __init__(self,y,t_time,screen,pygame,h = 20,l = 300):
        self.fixed_time = t_time
        self.time = t_time
        self.last_time = time.time()
        self.h = h
        self.r_l = l
        self.l = (self.time * (self.fixed_time/self.r_l)) * 10000
        self.x = screen.get_width()/2 - self.l/2
        self.y = y
        self.screen = screen
        self.pyg = pygame

    def update(self):
        self.pyg.draw.rect(self.screen,(0,20,255),(self.x,self.y,self.l,self.h))

        self.last_time = time.time()
        self.time = self.time - ((time.time() - self.last_time) * 1000)
        self.h = 30
        self.l = (self.fixed_time * (self.time/self.r_l)) * 10000
        self.x = self.screen.get_width()/2 - self.l/2
        print(self.l)