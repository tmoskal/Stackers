from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time

sense = SenseHat()
sense.clear()

class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640,480))
		self.gaming = True

	def startGame(self):
		pygame.time.set_timer(USEREVENT +1,800)
		x = 1
		p = 0
		while self.gaming:
			while True:
				sense.set_pixel(x,7,(0,0,225))
				x = x +1
				p = p +1
				time.sleep(.1)
				if p == 8:
					p = 0
				elif x == 8:
					x = 0
				sense.set_pixel(x,7,(0,0,225))
				sense.set_pixel(p,7,(0,0,0))
				
				
if __name__ == '__main__' : 
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()

