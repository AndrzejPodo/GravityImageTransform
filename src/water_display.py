import sys, pygame, time
import numpy as np
from LineOfDroplets import LineOfDroplets
from Image01 import Image01

def paused():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False
                    break
                
        clock.tick(15) 

vec = pygame.math.Vector2

V_0 = vec(0,1) # initial speed [m/s]
A = vec(0,30) # acceleration [m/(s^2)]
WATER_SCREEN_SIZE = (1000,700) #water screen dimension [cm]
PERIOD = 2 #how long a each line is resposible for state of valves [ms]

screen = pygame.display.set_mode((WATER_SCREEN_SIZE[0],WATER_SCREEN_SIZE[1])) #add 100 to height to make place for component at the top
water_screen = pygame.Surface(WATER_SCREEN_SIZE) #mulitply by 100 becuse we assume 1px=1cm 

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

# img = Image01("./src/arrow_tranformed.png")
img = Image01("./src/arrow.png")

lines = img.array01[::-1]
allsprites = pygame.sprite.RenderPlain()
clock = pygame.time.Clock()

screen.blit(background, (0, 0))
pygame.display.flip()


line_index = 0
last_line_change = int(round(time.time()*1000))
while 1:
    clock.tick(60)
    # checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused()
    # checking if we should consider next line
    if abs(last_line_change - int(round(time.time()*1000))) > PERIOD:
        last_line_change = int(round(time.time()*1000))
        line_index += 1
        line_index = line_index%len(lines)

    allsprites.add(LineOfDroplets(WATER_SCREEN_SIZE[0], lines[line_index], v0=V_0, a=A))
    allsprites.update()
    water_screen.blit(background, (0, 0))
    allsprites.draw(water_screen)
    screen.blit(water_screen, (0,100))
    pygame.display.flip()



