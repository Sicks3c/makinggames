import pygame
pygame.init()
soundObj = pygame.mixer.Sound('beep.wav')
soundObj.play()
import time
time.sleep(1)
soundObj.stop()