

import sys, math, pygame, vector, camera, poly, logs

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

		self.polyList = [
			poly.Poly([vector.Vector3(10,1,0), vector.Vector3(10,0,1), vector.Vector3(10,0,-1)])
		]

		for i in range(100):
			self.polyList.append(poly.Poly([
				vector.Vector3(10+5*math.sin(i/20),1+i/10,0), 
				vector.Vector3(10+5*math.sin(i/20),0,1+i/10), 
				vector.Vector3(10+5*math.sin(i/20),0,-1-i/10)
			]))

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


			logs.logList = []
			logs.log(round(self.clock.get_fps(), 2))
			logs.log(self.cam.pos)
			logs.log(self.cam.dir)

			self.screen.fill([150,250,250])
			self.cam.render(self.polyList)

			'''# Log vertices
			for poly in self.polyList:
				for vertex in poly.vertices:
					logs.log("Vertex: " + str(vertex))
				for vertex in poly.localVertices:
					logs.log("Local Vertex: " + str(vertex))
				for vertex in poly.viewVertices:
					logs.log("View Vertex: " + str(vertex))
			'''
			
			self.renderLogs()
			
			pygame.display.flip()

	def renderLogs(self):
		for k,string in enumerate(logs.logList):
			text = self.font_log.render(str(string), True, (0, 0, 0))
			self.screen.blit(text, [10,10+k*20])
