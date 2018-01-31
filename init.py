

import sys, math, pygame
pygame.init()

import vector, camera

res = [960, 540]
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

cam = camera.Camera(screen, res)

font = pygame.font.SysFont(None, 24)
#textrect = text.get_rect()
#textrect.centerx = screen.get_rect().centerx
#textrect.centery = screen.get_rect().centery

mouseLock = False



while True:
	dt = clock.tick()/1000
	if mouseLock:
		pygame.mouse.set_pos = (res[0]/2, res[1]/2)


	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				mouseLock = not mouseLock
				pygame.mouse.set_visible(not mouseLock)
	
	if pygame.key.get_pressed()[pygame.K_w]:
		cam.pos.x += 1 * dt

	screen.fill([150,250,250])
	cam.render()


	text = font.render(str(round(clock.get_fps(), 2)), True, (0, 0, 0))
	screen.blit(text, [10,10])

	text = font.render(str(cam.pos), True, (0, 0, 0))
	screen.blit(text, [10,30])

	print(mouseLock)

	pygame.display.flip()