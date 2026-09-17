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
            efect = intyfi(r'efect-(\d)',line)
            anim = intyfi(r'anim-(\d)',line)
            r = intyfi(r'r-(\d+)',line)
            g = intyfi(r'g-(\d+)',line)
            b = intyfi(r'b-(\d+)',line)
            dificalty = intyfi(r'd-(\d+)',line)
            e1 = stringyfi(r'e1-(\w)',line)
            e2 = stringyfi(r'e2-(\w)',line)
            e3 = stringyfi(r'e3-(\w)',line)

            level.append([pice_time,efect,anim,r,g,b,dificalty,e1,e2,e3])
load_level(1)


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
slider = elements.slider(60,1,screen,pygame)
e1_test = elements.rect(1,(0,30,255),65,2,pygame,screen)
e2_test = elements.rect(2,(0,30,255),65,2,pygame,screen)
e3_test = elements.rect(3,(0,30,255),65,2,pygame,screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    slider.update()
    e1_test.update()
    e2_test.update()
    e3_test.update()
    pygame.display.flip()
