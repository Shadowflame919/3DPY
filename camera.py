
import math, vector, pygame

class Camera():
    def __init__(self, screen, res):
        self.pos = vector.Vector3(0,0,0)
        self.dir = vector.Vector3(0,0,0)

        self.screen = screen    # Screen to render camera on
        self.res = res      # Resolution of camera

        self.fov = math.pi/3

    def render(self):   # Renders the camera's view on the screen

        # Crosshair
        pygame.draw.line(self.screen, [0,0,0], [self.res[0]/2-15,self.res[1]/2], [self.res[0]/2+15,self.res[1]/2], 3)
        pygame.draw.line(self.screen, [0,0,0], [self.res[0]/2,self.res[1]/2-15], [self.res[0]/2,self.res[1]/2+15], 3)


