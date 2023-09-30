class color:
    def __init__(self,color):
        print("color is",color)
class circle(color):
    def __init__(self,radius,color):        
        super().__init__(color)
        print("radius=",3.14*radius*radius)
class square(color):
    def __init__(self,color,side):
        super().__init__(color)
        print("area of square",side**2)
obj=circle(6,"red")     
obj=square("blue",4)   