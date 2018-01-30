
import math

class Vector3():
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def dotProduct(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z;

    def mag(self):
        return math.sqrt(self.dotProduct(self));

    def angleBetween(self, other):
        return math.acos(self.dotProduct(other) / (self.mag()*other.mag()));

    def normalised():
        mag = this.mag();
        return Vector3(this.x/mag, this.y/mag, this.z/mag)

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

    def log(self):
        print("(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")")

    def __str__(self):
        return ("(" + str(round(self.x,3)) + ", " + str(round(self.y,3)) + ", " + str(round(self.z,3)) + ")")