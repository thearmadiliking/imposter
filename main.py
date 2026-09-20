import pygame
import elements
import re
import math
import time

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('imposter')

font = pygame.font.SysFont(
    "Comic Sans MS",
    85,
    bold=True,
    italic=True
)
text = pygame.image.load("imposter.png")
text = pygame.transform.scale(text, (400, 80))

def intyfi(not_int,line):
    return int(str(re.findall(not_int,line)[0]))

def stringyfi(not_int,line):
    try:
        return str(re.findall(not_int,line)[0])
    except:
        return 0
    
def floatyfi(pattern, line):
    return float(re.findall(pattern, line)[0])



#level player
level_nmb = 1
def load_level(lvl_nmb):
    loaded_level = []
    with open(f'levels/{lvl_nmb}.lvl', 'r') as file:
        lines = file.readlines()
        for line in lines:
            pice_time = floatyfi(r'\d+(?:\.\d+)?',line)
            r = intyfi(r'r-(\d+)',line)
            g = intyfi(r'g-(\d+)',line)
            b = intyfi(r'b-(\d+)',line)
            dificalty = intyfi(r'd-(\d+)',line)
            e1 = stringyfi(r'e1-(\w)',line)
            e2 = stringyfi(r'e2-(\w)',line) or e1
            e3 = stringyfi(r'e3-(\w)',line) or e1

            loaded_level.append([e1,e2,e3,r,g,b,dificalty,pice_time])
    return loaded_level

level = load_level(level_nmb)

dic = {"r":elements.rect, "c":elements.circle}
class player():
    def __init__(self,lvl,numb = 0):
        global level_nmb, won
        if numb >= len(lvl):
            elements.finish_screen(won,len(lvl),screen,pygame)
            won = 0
            level_nmb += 1
            try:
                lvl = load_level(level_nmb)
            except FileNotFoundError:
                level_nmb = 1
                lvl = load_level(level_nmb)
            numb = 0
        self.lvl = lvl
        self.numb = numb
        self.line = lvl[numb]
        print(lvl[numb])
        self.imposter = elements.random.randint(1,3)
        self.e1 = dic[self.line[0]](1,(self.line[3],self.line[4],self.line[5]),self.line[6],self.imposter,pygame,screen)
        self.e2 = dic[self.line[0]](2,(self.line[3],self.line[4],self.line[5]),self.line[6],self.imposter,pygame,screen)
        self.e3 = dic[self.line[0]](3,(self.line[3],self.line[4],self.line[5]),self.line[6],self.imposter,pygame,screen)
        self.slider = elements.slider(60,self.line[7],screen,pygame)

    def next_line(self):
        self.numb += 1
        print(self.numb)
        self.__init__(self.lvl,numb=self.numb)

    def update(self,event):
        global last_event_importent 
        global won, level_nmb

        if self.slider.time <= 0:
            if event == self.imposter:
                last_event_importent = None
                won += 1
                self.next_line()
            else:
                last_event_importent = None
                self.next_line()

        self.slider.update()
        self.e1.update(last_event_importent)
        self.e2.update(last_event_importent)
        self.e3.update(last_event_importent)

#main menu loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False
            
    screen.fill((0, 0, 0))
    #render things
    angle = math.sin(time.time()) * 5
    rotated_text = pygame.transform.rotate(text, angle)
    text_rect = rotated_text.get_rect(center=(width / 2, height / 2 - 40))
    screen.blit(rotated_text, text_rect)
    pygame.display.flip() 


#game loop
running = True
line_nmb = 0
won = 0
lost = 0
events = {pygame.K_a: 1, pygame.K_DOWN: 2,
          pygame.K_s: 2, pygame.K_LEFT: 1,
          pygame.K_d: 3, pygame.K_RIGHT: 3}

pice = player(level)

last_event_importent = None
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in events:
                last_event_importent = events[event.key]

    screen.fill((0, 0, 0))
    pice.update(last_event_importent)
    pygame.display.flip()
