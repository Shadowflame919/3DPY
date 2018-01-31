
import math, logs

class Poly():
    def __init__(self, vertices):
        print(vertices)
        self.vertices = vertices
        self.localVertices = [None, None, None]  
        self.viewVertices = [None, None, None]
    
    def localiseVerticesToCamera(self, pos, direction):     # Finds the relative positions of each vertice to the camera (facing positive x)
        for i,vertex in enumerate(self.vertices):  
            # Firstly get relative position (simply position offset)
            self.localVertices[i] = vertex.sub(pos)

            # Rotate vector the opposite direction to camera's x
            self.localVertices[i].rotateAxisY(-direction.x)

            # Rotate vector the opposite direction to camera's y
            self.localVertices[i].rotateAxisZ(-direction.y)


    def calculateViewVertices(self, res, fov):
        for i,vertex in enumerate(self.localVertices):
            if (vertex.x < 0):
                self.viewVertices[i] = False
            else:
                self.viewVertices[i] = [
                    round((res[0]/2) + (res[0]/2)*((vertex.z / vertex.x) / math.tan(fov/2))),
                    round((res[1]/2) - (res[1]/2)*((vertex.y / vertex.x) / math.tan((9/16)*fov/2)))
                ]



"""


"""