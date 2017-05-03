import pygame
import sys
from Window import Window

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
font = pygame.font.SysFont(None, 18) #arguments are (name, size, bold=True/False, italic=True/False)

x = Window(1280,720,"Ship Zone",0,0,0,True,black,white,font)
x.load()

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
	
	x.render(screen)

	#update display
	pygame.display.flip()

	#update tick and playtime
	playtime += ms / 1000.0 #adds ms to playtime and then divides it by 1000 for the time elapsed in seconds.
	tick=tick+1

pygame.quit()

#end of program reports
print(str(tick))
print(playtime)