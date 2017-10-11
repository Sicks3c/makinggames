import pygame, sys # import the module pygame and sys 
from pygame.locals import * # this line tells python to display and run all the modules (*) in pygame.locals instead of calling each one by one

pygame.init() # make sure to run this before calling any pygame method 
DISPLAYSURF = pygame.display.set_mode((400, 300)) # this line tells python to display a screen with width 400 px and height of 300
pygame.display.set_caption('Hello world') # this line tells python to set a caption -title- hello world
while True:  # this is an infinite loop which make the game run until there's a break or sys.exit called
			 #this method is called to make sure when the game is launched the updates comes throught to make changes
			 # and the game still running white the changed made by user ,

	for event in pygame.event.get(): #Its a loop created with a variable named event will ne assigned to the value of the next even object in the List 

			


		if event.type == QUIT:# even.type is a method that calls quit or pygame.locals.quit , since we imported it before 
			pygame.quit()# we tell pygame to quit
			sys.exit()# since idle has a bug we pygame.quit 
	pygame.display.update()# this tell python to run what we did in pygame.display and it to screen


#	A Reminder About Functions, Methods, Constructor Functions, and Functions in Modules (and the Difference Between Them)
#   foo() = call of a function named foo
#	duckine.foo() = call of a method named foo which is attached to an object stored in a variable named duckie
#	Constructor function : is the same as a normal function call like foo() but it's return value is a new object and they start by Capital letter
#	Example : pygame.Rect()  ||  pygame.Surface() ~~~~ They return newRect and Surface objects


#
