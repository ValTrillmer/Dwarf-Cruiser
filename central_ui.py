import pygame
import sys
from Window import Display
from Mode import Main_Mode
import Formatting_Data as F

#import engine (whatever that engine may be)

#This file holds the main game loop


#initializes pygame
pygame.init()
F.set_font()


#create clock object
clock = pygame.time.Clock()

#frame rate
fps = 30

#seconds game is played. It's a counter for potential future purposes. Numnber is a float.
playtime = 0.0


screen = pygame.display.set_mode((1280, 720)) #set screen size

mode = Main_Mode()

mode.load_window()
mode.load_ship()
mode.load_character()
mode.create_character_display()
mode.create_tablet()



mainloop = True
tick = 0
while mainloop:

	#amount of time elapse since last tick
	ms = clock.tick(fps)

	#game logic
	mode.run_engine()

	#event handler
	mainloop = mode.handle_event()

	
	mode.compile_screen(screen)
	#mode.draw_heart(screen)

	#update display
	pygame.display.flip()

	#update tick and playtime
	playtime += ms / 1000.0 #adds ms to playtime and then divides it by 1000 for the time elapsed in seconds.
	tick=tick+1

pygame.quit()

#end of program reports
print(str(tick))
print(playtime)