
import math, vector, pygame

class Camera():
    def __init__(self, screen, res):
        self.pos = vector.Vector3(0,0,0)

        # Not actually a vector, x represents looking right/left, y is up/down, z is just rotating view
        # Default (0,0,0) is looking in the positive x direction (left handed coordinate system)
        self.dir = vector.Vector3(0,0,0)    

        self.screen = screen    # Screen to render camera on
        self.res = res      # Resolution of camera

        self.fov = math.pi/3

        self.speed = 10

    def render(self):   # Renders the camera's view on the screen

        # Crosshair
        pygame.draw.line(self.screen, [0,0,0], [self.res[0]/2-15,self.res[1]/2], [self.res[0]/2+15,self.res[1]/2], 3)
        pygame.draw.line(self.screen, [0,0,0], [self.res[0]/2,self.res[1]/2-15], [self.res[0]/2,self.res[1]/2+15], 3)

    def changePos(self, dt, pressedKeys):
        if pressedKeys[pygame.K_w]:
            self.pos.x += dt * self.speed * math.cos(self.dir.x)
            self.pos.z += dt * self.speed * math.sin(self.dir.x)
        if pressedKeys[pygame.K_s]:
            self.pos.x -= dt * self.speed * math.cos(self.dir.x)
            self.pos.z -= dt * self.speed * math.sin(self.dir.x)
        if pressedKeys[pygame.K_a]:
            self.pos.x -= dt * self.speed * math.sin(self.dir.x)
            self.pos.z += dt * self.speed * math.cos(self.dir.x)
        if pressedKeys[pygame.K_d]:
            self.pos.x += dt * self.speed * math.sin(self.dir.x)
            self.pos.z -= dt * self.speed * math.cos(self.dir.x)
        if pressedKeys[pygame.K_SPACE]:
            self.pos.y += dt * self.speed
        if pressedKeys[pygame.K_LSHIFT]:
            self.pos.y -= dt * self.speed

    def changeDir(self, mouseMove):
        if mouseMove[0] != 0:
            self.dir.x -= mouseMove[0] / 1000
            if (self.dir.x < -math.pi): 
                self.dir.x += 2*math.pi
            elif (self.dir.x > math.pi): 
                self.dir.x -= 2*math.pi

        if mouseMove[1] != 0:
            self.dir.y -= mouseMove[1] / 1000
            if (self.dir.y > math.pi/2): 
                self.dir.y = math.pi/2
            elif (self.dir.y < -math.pi/2): 
                self.dir.y = -math.pi/2
