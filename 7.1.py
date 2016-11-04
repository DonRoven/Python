import math

class Sphere():
    
    def __init__(self, r = 1, x = 0, y = 0, z = 0):
        self._r = r
        self._x = x
        self._y = y
        self._z = z

    def get_volume(self):
        return ((4/3)*math.pi*(self._r**3))

    def get_square(self):
        return (4*math.pi*(self._r**2))

    def get_radius(self):
        return (self._r)
    
    def get_center(self):
        return ((self._x, self._y, self._z))

    def set_radius(self, r):
        self._r = r

    def set_center(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def is_point_inside(self, x, y, z):
        if math.sqrt((self.x - x)**2 + (self.y - y)**2 + (self.z - z)**2) <= self.r**2:
            return True
        else:
            return False

if __name__ == '__main__':
    # simple module test like
    s = Sphere()
    assert s.r == 1.0
    assert not s.is_point_inside(1.0, 1.0, 1.0)

###
#import math

#class Sphere(object):
#    center = {'x':0, 'y':0, 'z':0}
#    radius = 1
    
#    def __init__(self, r = 1, x = 0, y = 0, z = 0):
#        self.set_radius(r)
#        self.set_center(x, y, z)
        
#    def get_volume(self):
#        return 4.0 / 3 * math.pi * self.radius ** 3
        
#    def get_square(self):
#        return 4.0 * math.pi * self.radius ** 2
#        
#    def set_radius(self, r):
#        self.radius = r
        
#    def set_center(self, x = 0, y = 0, z = 0):
#        self.center['x'] = x
#        self.center['y'] = y
#        self.center['z'] = z
        
#    def get_radius(self):
#        return self.radius * 1.0
        
#    def get_center(self):
#        return (self.center['x'] * 1.0, self.center['y'] * 1.0, self.center['z'] * 1.0)
        
#    def is_point_inside(self, x = 0, y = 0, z = 0):
#        distance = math.sqrt((self.center['x'] - x)**2 + 
#                            (self.center['y'] - y)**2 + 
#                            (self.center['z'] - z)**2)
#        return distance < self.radius
###