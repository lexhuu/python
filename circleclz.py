class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        self.area= 3.14*(self.radius**2)
        return self.area
    def circum(self):
        self.circum= 2 * 3.14 * self.radius
        return self.circum
        
r=int(input("Enter the radius of the circle"))
calc = circle(r)
print("The area of the circle is:",calc.area())
print("The circumference of the circle is:",calc.circum())