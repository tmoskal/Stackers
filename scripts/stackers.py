from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
from getpass import getpass
sense = SenseHat()
sense.clear()
colors = [(225,0,0),(255,170,0),(255,255,0),(0,255,0),(0,0,255),(119,0,179),(255,0,214),(255,0,0)]
rows = []
class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640,480))
		self.gaming = True

	def startGame(self):
		pygame.time.set_timer(USEREVENT +1,800)
		x = 0
		speed = .3
		y = 7
		n = 0
		p = 0
		z = 0
		while self.gaming:
		
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if y == -1:
						sense.clear()
						sense.show_message("Winner", 0.1, text_colour=(0,255,0), back_colour=(0,0,0))
						sense.clear()
						exit()	
					if y == 7:
						rows.append(x)
						p = p + 1
					if x == 0:
						x = 8
						sense.set_pixel(x-1,y,(colors[n]))
						y = y-1
						x = 0
						n = n + 1
						
						
					else:
						sense.set_pixel(x-1,y,colors[n])
						y = y-1
						n = n + 1
			
					
					if(y < 7):
						rows.append(x)
						if(rows[p] > rows[z]):
							time.sleep(2)
							sense.clear()
							sense.show_message("Game Over", 0.1, text_colour=(0,255,0), back_colour=(0,0,0))
							sense.clear()
							exit()
						elif(rows[p] < rows[z]):
							time.sleep(2)
							sense.clear()
							sense.show_message("Game Over", 0.1, text_colour=(0,255,0), back_colour=(0,0,0))
							sense.clear()
							exit()
						else:
							p = p + 1
							z = z + 1		
						

					
				else:
					if y == -1:
						sense.clear()
						sense.show_message("Winner", 0.05, text_colour=(0,255,0), back_colour=(0,0,0))
						sense.clear()
						exit()
					sense.set_pixel(x,y,(225,225,225))
					time.sleep(speed)
					sense.set_pixel(x,y,(0,0,0))
					time.sleep(speed)
					if x < 8:
						x = x + 1
					if x == 8:
						x = 0
				
if __name__ == '__main__' : 
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()

