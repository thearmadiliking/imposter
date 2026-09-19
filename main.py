import pygame
import elements
import re

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
text = font.render('Impster', True, (230,10,15))

def intyfi(not_int,line):
    return int(str(re.findall(not_int,line)[0]))

def stringyfi(not_int,line):
    try:
        return str(re.findall(not_int,line)[0])
    except:
        return 0


#level player
level = []
def load_level(lvl_nmb):
    with open(f'levels/{lvl_nmb}.lvl', 'r') as file:
        lines = file.readlines()
        for line in lines:
            pice_time = intyfi(r'time-(\d)',line)
            r = intyfi(r'r-(\d+)',line)
            g = intyfi(r'g-(\d+)',line)
            b = intyfi(r'b-(\d+)',line)
            dificalty = intyfi(r'd-(\d+)',line)
            e1 = stringyfi(r'e1-(\w)',line)
            e2 = stringyfi(r'e2-(\w)',line)
            e3 = stringyfi(r'e3-(\w)',line)

            level.append([e1,e2,e3,r,g,b,dificalty,pice_time])
load_level(1)

dic = {"r":elements.rect}
class player():
    def __init__(self,line):
        self.line = line
        self.imposter = elements.random.randint(0,3)
        self.e1 = dic[line[0]](1,(line[3],line[4],line[5]),line[6],self.imposter,pygame,screen)
        self.e2 = dic[line[0]](2,(line[3],line[4],line[5]),line[6],self.imposter,pygame,screen)
        self.e3 = dic[line[0]](3,(line[3],line[4],line[5]),line[6],self.imposter,pygame,screen)
        self.slider = elements.slider(60,line[7],screen,pygame)


    def update(self):
        self.e1.update()
        self.e2.update()
        self.e3.update()
        self.slider.update()


#main menu loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False
            
    screen.fill((0, 0, 0))
    #render things
    screen.blit(text,(width/2-120,height/2-80))
    pygame.display.flip() 


#game loop
running = True
line_nmb = 0

pice = player(level[0])
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pice.update()
    pygame.display.flip()
