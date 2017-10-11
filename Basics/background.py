import pygame, sys
from pygame.locals import *

pygame.init()

pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1, 0.0)

DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	for event in pygame.event.get():
		if event.type == QUIT:
			soundObj = pygame.mixer.Sound('beep.wav')
			soundObj.play()
			import time
			time.sleep(1)
			soundObj.stop()
			pygame.mixer.music.stop()
			pygame.quit()
			sys.exit()

	pygame.display.update()
