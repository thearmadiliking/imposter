
def up(pygame):
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                pygame.quit()
                quit()

def default(pygame,screen,e1_x,e2_x,e3_x,bar = False):
    screen.fill((25,5,30))
    pygame.draw.rect(screen,(20,150,200),(e1_x,100,246.666,400))
    pygame.draw.rect(screen,(20,110,180),(e2_x,100,246.666,400))
    pygame.draw.rect(screen,(20,150,200),(e3_x,100,246.666,400))
    if bar:
        pygame.draw.rect(screen,(0,20,255),(screen.get_width()/2 - 300/2,60,300,20))
    pygame.display.flip()

def run(pygame,screen,time,elements):
    #rainbow animations form (25,5,30) and end with (25,5,30)
    for i in range(200):
        screen.fill((i,0,200-i))
        up(pygame)
        time.sleep(0.005)
    
    for i in range(200):
        screen.fill((200-i,0,i))
        up(pygame)
        time.sleep(0.005)

    for i in range(170):
        screen.fill((25,5,200-i))
        up(pygame)
        time.sleep(0.005)

    screen.fill((25,5,30))
    up(pygame)
    time.sleep(1)

    e1_x = 20
    e2_x = 276.666
    e3_x = 533.333
    pygame.draw.rect(screen,(20,150,200),(e1_x,100,246.666,400))
    up(pygame)
    time.sleep(0.2)
    pygame.draw.rect(screen,(20,110,180),(e2_x,100,246.666,400))
    up(pygame)
    time.sleep(0.2)
    pygame.draw.rect(screen,(20,150,200),(e3_x,100,246.666,400))
    up(pygame)
    time.sleep(2)

    for i in range(3):
        pygame.draw.rect(screen,(20,200,100),(e1_x-5,100-5,246.666+10,400+10))
        pygame.draw.rect(screen,(20,150,200),(e1_x,100,246.666,400))
        pygame.draw.rect(screen,(20,200,100),(e3_x-5,100-5,246.666+10,400+10))
        pygame.draw.rect(screen,(20,150,200),(e3_x,100,246.666,400))
        up(pygame)

        time.sleep(0.2)

        default(pygame,screen,e1_x,e2_x,e3_x)
        up(pygame)

        time.sleep(0.2)

    time.sleep(1.5)

    for i in range(3):
        pygame.draw.rect(screen,(20,200,100),(e2_x-5,100-5,246.666+10,400+10))
        pygame.draw.rect(screen,(20,110,180),(e2_x,100,246.666,400))
        up(pygame)

        time.sleep(0.2)

        default(pygame,screen,e1_x,e2_x,e3_x)

        up(pygame)

        time.sleep(0.2)

    time.sleep(1.5)

    for i in range(2):
        pygame.draw.rect(screen,(0,20,255),(screen.get_width()/2 - 300/2,60,300,20))
        up(pygame)
        time.sleep(0.2)
        default(pygame,screen,e1_x,e2_x,e3_x)
        time.sleep(0.2)

    pygame.draw.rect(screen,(0,20,255),(screen.get_width()/2 - 300/2,60,300,20))
    up(pygame)
    time.sleep(3)
    for i in range(2):
        pygame.draw.rect(screen,(20,200,100),(e1_x-5,100-5,246.666+10,400+10))
        pygame.draw.rect(screen,(20,150,200),(e1_x,100,246.666,400))
        up(pygame)
        time.sleep(0.2)
        default(pygame,screen,e1_x,e2_x,e3_x,bar = True)
        up(pygame)
        time.sleep(0.2)
    time.sleep(1)
    for i in range(2):
        pygame.draw.rect(screen,(20,200,100),(e2_x-5,100-5,246.666+10,400+10))
        pygame.draw.rect(screen,(20,150,200),(e2_x,100,246.666,400))
        up(pygame)
        time.sleep(0.2)
        default(pygame,screen,e1_x,e2_x,e3_x,bar = True)
        up(pygame)
        time.sleep(0.2)
    time.sleep(1)
    for i in range(2):
        pygame.draw.rect(screen,(20,200,100),(e3_x-5,100-5,246.666+10,400+10))
        pygame.draw.rect(screen,(20,150,200),(e3_x,100,246.666,400))
        up(pygame)
        time.sleep(0.2)
        default(pygame,screen,e1_x,e2_x,e3_x,bar = True)
        up(pygame)
        time.sleep(0.2)
    time.sleep(1)
    time.sleep(10)


if __name__ == "__main__":
    import pygame
    import time
    import elements
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    run(pygame,screen,time,elements)