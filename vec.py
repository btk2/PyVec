import math


class vec:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    def __str__(self):
        return "[" + str(self.x) +", "+str(self.y)+", " + str(self.z) + "]" 
        
    def __getitem__(self, key):
        if key ==0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z
        else:
            raise IndexError("Vector index out of range")
            
    def __bool__(self):
        return (self.x != 0) and (self.y != 0) and (self.z != 0)
            
    def mag(self):
            return((self.x ** 2) + (self.y ** 2) + (self.z ** 2))** 0.5
        
    def __add__(self, other):
        if isinstance(other, vec):
            return vec(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, float) or isinstance(other, int):
            return vec(self.x + other, self.y + other, self.z + other)
        
    def __iadd__(self, other):
        if isinstance(other, vec):
            return vec(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, float) or isinstance(other, int):
            return vec(self.x + other, self.y + other, self.z + other)
        
    def __sub__(self, other):
        if isinstance(other, vec):
            return vec(self.x - other.x, self.y - other.y, self.z - other.z)
        if isinstance(other, float) or isinstance(other, int):
            return vec(self.x - other, self.y - other, self.z - other)
            
    def __rsub__(self, other):
        if isinstance(other, vec):
            return vec(other.x - self.x, other.y - self.y, other.z - self.z)
        if isinstance(other, float) or isinstance(other, int):
            return vec(other - self.x, other - self.y, other - self.z)
        
    # Scaler Multiplication and Dot product
    def __mul__(self, other):
        if isinstance(other, vec):
            return (self.x * other.x + self.y * other.y + self.z * other.z)
        if isinstance(other, float) or isinstance(other, int):
            return vec(self.x * other, self.y * other, self.z * other)
            
    def __truediv__(self, other):
        if isinstance(other, vec):
            return vec(self.x / other.x, self.y / other.y, self.z / other.z)
        if isinstance(other, float) or isinstance(other, int):
            return vec(self.x / other, self.y / other, self.z / other)
            
    def __mod__(self, other):
        if isinstance(other, vec):
            return vec(self.x % other.x, self.y % other.y, self.z % other.z)
        if isinstance(other, float) or isinstance(other, int):
            return vec(self.x % other, self.y % other, self.z % other)
            
    def __neg__(self):
        return vec((-1)*self.x, (-1)*self.y, (-1)*self.z)
            
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
        
    def __ne__(self, other):
        return (self.x != other.x) or (self.y != other.y) or (self.z != other.z)
        
    def unit(self):
        return self / self.mag()
        
    def cross(self, other):
        return vec(self.y * other.z - self.z*other.y, self.z * other.x - self.x*other.z, self.x * other.y - self.y*other.x)
    
    def angle(self, other):
        return math.acos((self * other) / ( self.mag() * other.mag()))
        
