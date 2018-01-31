

import sys, math, pygame
pygame.init()

import vector, camera


class Main():
	def __init__(self):
		self.res = (960, 540)
		self.screen = pygame.display.set_mode(self.res)
		self.clock = pygame.time.Clock()

		self.cam = camera.Camera(self.screen, self.res)

		self.font_log = pygame.font.SysFont(None, 24)
		#textrect = text.get_rect()
		#textrect.centerx = screen.get_rect().centerx
		#textrect.centery = screen.get_rect().centery

		self.mouseLock = False

	def start(self):	# Starts the main update loop
		while True:
			dt = self.clock.tick()/1000
			if self.mouseLock:
				pygame.mouse.set_pos = (self.res[0]/2, self.res[1]/2)

			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.mouseLock = not self.mouseLock
						pygame.mouse.set_visible(not self.mouseLock)
						pygame.event.set_grab(self.mouseLock)
				if event.type == pygame.MOUSEMOTION:
					if self.mouseLock:
						self.cam.changeDir(event.rel)
			
			# Moves camera
			if self.mouseLock:
				self.cam.changePos(dt, pygame.key.get_pressed())

			self.screen.fill([150,250,250])
			self.cam.render()


			text = self.font_log.render(str(round(self.clock.get_fps(), 2)), True, (0, 0, 0))
			self.screen.blit(text, [10,10])

			text = self.font_log.render(str(self.cam.pos), True, (0, 0, 0))
			self.screen.blit(text, [10,30])

			text = self.font_log.render(str(self.cam.dir), True, (0, 0, 0))
			self.screen.blit(text, [10,50])

			pygame.display.flip()


main = Main()
main.start()



