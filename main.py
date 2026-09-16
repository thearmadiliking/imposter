import pygame
import elements
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

#main menu loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    #render things
    screen.blit(text,(width/2-120,height/2-80))
    pygame.display.flip() 


#game loop
running = True
slider = elements.slider(60,1,screen,pygame)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    slider.update()
    pygame.display.flip()
