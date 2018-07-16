import pygame

import sys

import time

from pygame.locals import *



pygame.init()

pygame.display.set_caption("Basics")

screen = pygame.display.set_mode((500,400))



# Define variables

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

GREEN = (0, 255, 0)

RED = (255, 0, 0)
x=250
while True:

	for event in pygame.event.get():

		if event.type == K_RIGHT:
			 x = x+5
       
      

pygame.draw.rect(screen, RED,[x, 390, 100, 10])
 
while True:

	for event in pygame.event.get():

		if event.type == QUIT:

			pygame.quit()

			sys.exit()

			#### Respond to events



	#### Make animations

	

	#### Update display

	pygame.display.update()

	time.sleep(0.001)