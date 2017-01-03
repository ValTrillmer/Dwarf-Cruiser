import pygame
import dwarf_engine
from dwarf_engine import active_ships

pygame.init()

screen = pygame.display.set_mode((1280,720)) #set screen size
basicfont = pygame.font.SysFont(None, 24)
# create clock object
clock = pygame.time.Clock()
#desired frame rate
FPS = 30
# how many seconds game is played
playtime = 0.0

def make_surface(width,height):
	surf = pygame.Surface((width,height)) # create empty pygame surface
	surf.fill((0,0,0)) #fill brackground with black colour
	surf = surf.convert() #convert Surface to make blitting faster
	return surf

def make_text(string):
	text = basicfont.render(string, True, (255, 255, 255), (0,0,0))
	return text

def centre_text(surface,text):
	return (surface.get_width()-text.get_width())/2



#display functions
def ship_display():
	ship_zone.fill((0,0,0))
	t = make_text("ship zone")
	ship_zone.blit(t, (centre_text(ship_zone,t),0))
	ship_zone.blit(make_text(active_ships[0].name), (0,24))
	ship_zone.blit(make_text("Power: "+str(active_ships[0].systems[2].reserve)+"/"+str(active_ships[0].systems[2].output)), (0,48))
	h=0
	for s in active_ships[0].layout:
		room = make_text(s.name)
		ship_zone.blit(room, (0,72+(basicfont.get_height()*h)))
		h=h+1

def crew_display():
	crew_zone.fill((0,0,0))
	t = make_text("crew zone")
	crew_zone.blit(t, (centre_text(crew_zone,t),0))
	h=0	
	for c in active_ships[0].crew:
		crew_d = make_surface(crew_zone.get_width(),basicfont.get_height()*2)
		name = c.name
		hp = str(c.vitals)
		location = c.room.name
		feed = make_text(name+" "+hp+" "+location)
		action = make_text("Action: "+str(c.action))
		crew_d.blit(feed, (0,0))
		crew_d.blit(action, (0,basicfont.get_height()))
		crew_zone.blit(crew_d, (0,basicfont.get_height()+(crew_d.get_height()*h)))
		h=h+1

def system_display():
	system_zone.fill((0,0,0))
	t = make_text("system zone")
	system_zone.blit(t, (centre_text(system_zone,t),0))
	h=0
	for s in active_ships[0].systems:
		name = s.name
		hp = str(s.hp)
		power = str(s.p)
		feed = make_text(name+" "+hp+" "+power)
		system_zone.blit(feed, (0,24+(basicfont.get_height()*h)))
		h=h+1

def oxy_display():
	oxy_zone.fill((0,0,0))
	t = make_text("Oxygen")
	oxy_zone.blit(t, (centre_text(oxy_zone,t),0))
	h=0
	for r in active_ships[0].layout:
		name = r.name
		oxy = str(r.oxygen)
		feed = make_text(name+" "+oxy)
		oxy_zone.blit(feed, (0,24+(feed.get_height()*h)))
		h=h+1



ship_zone = make_surface(640,360)
crew_zone = make_surface(640,360)
system_zone = make_surface(640,360)
oxy_zone = make_surface(640,360)

mainloop = True
tick = 0
while mainloop:
	#understanding time
	milliseconds = clock.tick(FPS) #apparently do not go faster than this


	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			mainloop = False #pygame window closed by user
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				mainloop = False #user pressed ESC

	#tick
	dwarf_engine.update(tick)

	#print frame rate and play time in titlebar
	playtime += milliseconds / 1000.0 #adds seconds to playtime
	#calculates the number of seconds passed (by divding by 1000.0) and increases the value of the variable playtime
	caption = "FPS: {0:.2f}	Playtime: {1:.2f}".format(clock.get_fps(), playtime)
	pygame.display.set_caption(caption)

	#blitting text
	ship_display()
	crew_display()
	system_display()
	oxy_display()

	#blitting background
	screen.blit(ship_zone, (0,0))
	screen.blit(crew_zone, (640,0))
	screen.blit(system_zone, (0,360))
	screen.blit(oxy_zone, (640,360))
	pygame.display.flip()

	tick=tick+1

pygame.quit()

print("This game was played for {0:.2f} seconds".format(playtime))