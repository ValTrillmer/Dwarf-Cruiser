import pygame
import sys
from Window import Display
from Mode import Main_Mode

#import engine (whatever that engine may be)

#This file holds the main game loop


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

mode.load_window()

mainloop = True
tick = 0
while mainloop:

	#amount of time elapse since last tick
	ms = clock.tick(fps)

	#event handler
	mainloop = mode.handle_event()

	
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