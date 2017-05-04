import pygame
import sys
from Window import Window
from Mode import Main_Mode

#import engine (whatever that engine may be)

#This file holds the main game loop

#colour data
white = (255,255,255)
black = (0,0,0)

#initializes pygame
pygame.init()

#create clock object
clock = pygame.time.Clock()

#frame rate
fps = 30

#seconds game is played. It's a counter for potential future purposes. Numnber is a float.
playtime = 0.0


screen = pygame.display.set_mode((1280, 720)) #set screen size

mode = Main_Mode()

mode.load_windows()

mainloop = True
tick = 0
while mainloop:
	#amount of time elapse since last tick
	ms = clock.tick(fps)

	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			mainloop = False #pygame window closed by user
		elif event.type == pygame.KEYDOWN: #should be all caps
			if event.key == pygame.K_ESCAPE:
				mainloop = False #user pressed ESC
			if event.key == pygame.K_m:
				if mode.tablet.visible == True:
					mode.tablet.visible = False
				else:
					mode.tablet.visible = True
	
	mode.compile_screen(screen)

	#update display
	pygame.display.flip()

	#update tick and playtime
	playtime += ms / 1000.0 #adds ms to playtime and then divides it by 1000 for the time elapsed in seconds.
	tick=tick+1

pygame.quit()

#end of program reports
print(str(tick))
print(playtime)