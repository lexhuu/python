import math

class con():
    def __init__(self,real,img=0.0):
        self.real=real
        self.img=img
        
    def __add__(self, other):
        return complex(self.real + other.real,self.img + other.img)
    
    def __sub__(self, other):
        return complex(self.real - other.real,self.img - other.img)
    
    def __mul__(self, other):
        return complex(self.real * other.real - self.img * other.img, self.img * other.real + self.real * other.img)
    
    def __abs__(self):
        return math.sqrt(self.real**2 + self.img**2)
    
    def __neg__(self):
        return complex(-self.real,-self.img) #-1*self.real,-1*self.img
    
    def __eq__(self, other):
        return self.real == other.real and self.img == other.img
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return '(%g,%g)' % (self.real, self.img)
    
    def __div__(self, other):
        return complex(self.real / other.real - self.img * other.img, self.img * other.real + self.real / other.img)
    
c1=con(2,3)
c2=con(1,2)
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(abs(c1))
print(c1==c2)
print(c1!=c2)
print(-c1)
print(str(c1))