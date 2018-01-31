
import math, logs

class Vector3():
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return ("(" + str(round(self.x,3)) + ", " + str(round(self.y,3)) + ", " + str(round(self.z,3)) + ")")

    def log(self):
        print(str(self))

    def add(self, other):     # Returns a vector which is the sum of itself and another vector
        return Vector3(
            self.x + other.x, 
            self.y + other.y, 
            self.z + other.z
        )

    def sub(self, other):     # Returns a vector which represents itself minus another vector
        return Vector3(
            self.x - other.x, 
            self.y - other.y, 
            self.z - other.z
        )

    def dotProduct(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z;

    def mag(self):
        return math.sqrt(self.dotProduct(self));

    def angleBetween(self, other):
        return math.acos(self.dotProduct(other) / (self.mag()*other.mag()));

    def normalised(self):
        mag = this.mag();
        return Vector3(this.x/mag, this.y/mag, this.z/mag)

    def rotateAxisY(self, angle):  # Rotates vector anticlockwise around the y axis
        newX = math.cos(angle)*self.x - math.sin(angle)*self.z
        newZ = math.sin(-angle)*self.x - math.cos(-angle)*self.z
        self.x = newX
        self.z = newZ

    def rotateAxisZ(self, angle):  # Rotates vector anticlockwise around the z axis
        newX = math.cos(angle)*self.x - math.sin(angle)*self.y
        newY = math.sin(angle)*self.x + math.cos(angle)*self.y
        self.x = newX
        self.y = newY

