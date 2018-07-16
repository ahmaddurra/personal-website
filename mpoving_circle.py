

import pygame
import sys
import time
from pygame.locals import *
pygame.init()
pygame.display.set_caption("pac_man")
screen = pygame.display.set_mode((500,400))# Define variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
direction = "forward"
direction2= "down"
x = 160
y=150
pygame.draw.rect(screen, GREEN,(x, 150, 100, 100), 0)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            #### Respond to events
    screen.fill(BLACK)
    if (direction == "forward"):
        x = x+5
       
        if (x >= 400):
            direction ="backward"
        # if(y>=300):
        #     direction = "forward" 
    elif(direction == "backward"):
        x = x-5
        
        if (x <= 100):
            direction = "forward"
        # if(y <= 100)  
        #     direction = "forward"
    if(direction2=="down"):
        y=y+5
        if(y>=300):
            direction2="up"
    elif(direction2=="up"):
        y=y-5
        if(y<=100):
            direction2="down"





    pygame.draw.circle(screen, RED, [x,y], 100, 0)      
    #### Make animations    #### Update display
    pygame.display.update()
    
    time.sleep(0.01)