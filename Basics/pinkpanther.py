import pygame, sys
from pygame.locals import *

pygame.init()

pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1, 0.0)
FPS = 30 
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Pink')

WHITE = (255, 255, 255)
catImg = pygame.image.load('small.jpg')
catx = 10
caty = 10

direction = 'right'

while True:
	DISPLAYSURF.fill(WHITE)

	if direction == 'right':
		catx += 5
		if catx == 280:
			direction = 'down'

	elif direction == 'down':
		caty += 5
		if caty == 220:
			direction = 'left'

	elif direction == 'left':
		catx -= 5
		if catx == 10:
			direction == 'up'

	elif direction == 'up':
		caty -= 5
		if caty == 10:
			direction = 'right'

	DISPLAYSURF.blit(catImg,(catx, caty))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.mixer.music.stop()
			pygame.quit()
			sys.exit()
	pygame.display.update()
	fpsClock.tick(FPS)