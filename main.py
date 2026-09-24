import pygame
import elements
import re
import math
import time
import os
from pygame import mixer
import tutorial

#setup pygame-mixer to play the main theam song
pygame.init()
mixer.init()

mixer.music.load("track/main.mp3")
mixer.music.play(-1)
mixer.music.set_volume(1)

#set the max fps for consistent speeds
clock = pygame.time.Clock()
clock.tick(60)

#window setings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('imposter')

#loading the text
text = pygame.image.load("imposter.png")
text = pygame.transform.scale(text, (400, 80))

#Function for formating the data from the .lvl files
def intyfi(not_int,line):
    return int(str(re.findall(not_int,line)[0]))

def stringyfi(not_int,line):
    try:
        return str(re.findall(not_int,line)[0])
    except:
        return 0
    
def floatyfi(pattern, line):
    return float(re.findall(pattern, line)[0])

def parse_color(line, name):
    match = re.search(rf'{name}-\(([^)]+)\)', line)
    if not match:
        return None
    values = [int(part.strip()) for part in match.group(1).split(',')]
    return tuple(values)

#read levels
def read_levels():
    lvls = []
    colors = []
    secenderys = []

    for filename in os.listdir('levels'):
        #filter the lvl files from the uther files
        if filename.endswith('.lvl'):
            with open(os.path.join('levels', filename), 'r') as file:
                #read the files 
                lines = file.readlines()
                for line in lines:
                    main_color = parse_color(line, 'main')
                    second_color = parse_color(line, 'second')
                    if main_color is None or second_color is None:
                        continue
                    lvls.append(filename[:-4])
                    colors.append(main_color)
                    secenderys.append(second_color)
    return lvls, colors, secenderys

lvls, colors, secenderys = read_levels()

#level player
level_nmb = 1
def load_level(lvl_nmb,lvls):
    loaded_level = []
    with open(f'levels/{lvls[lvl_nmb]}.lvl', 'r') as file:
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

dic = {"r":elements.rect, "c":elements.circle}

#this is the main level player 
class player():
    def __init__(self,lvl,numb = 0):
        global level_nmb, won
        if numb >= len(lvl):
            elements.finish_screen(won,len(lvl),screen,pygame,math)
            won = 0
            lvl = load_level(elements.lvl_picker(lvls,colors,secenderys,screen,pygame),lvls)
            numb = 0
        self.lvl = lvl
        self.numb = numb
        self.line = lvl[numb]
        self.imposter = elements.random.randint(1,3)
        self.e1 = dic[self.line[0]](1,(self.line[3],self.line[4],self.line[5]),self.line[6],self.imposter,pygame,screen)
        self.e2 = dic[self.line[0]](2,(self.line[3],self.line[4],self.line[5]),self.line[6],self.imposter,pygame,screen)
        self.e3 = dic[self.line[0]](3,(self.line[3],self.line[4],self.line[5]),self.line[6],self.imposter,pygame,screen)
        self.slider = elements.slider(60,self.line[7],screen,pygame)

    def next_line(self):
        self.numb += 1
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
mixer.quit()
mixer.init()
#mixer.music.load("track/totorial.mp3")
#mixer.music.play(1)
#mixer.music.set_volume(1)
tutorial.run(pygame,screen,time,elements)

level_nmb = elements.lvl_picker(lvls,colors,secenderys,screen,pygame)
level = load_level(level_nmb,lvls)

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
