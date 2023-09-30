class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name) 
        print("age:",self.age)   
class student(Person):
    def __init__(self,rollno,name,age,per):
        self.rollno=rollno
        super(). __init__(name,age) 
        self.per=per
    def display(self):
        print('Rollno:',self.rollno)
        super().display()
        print("percentage:",self.per)
s1=student(101,'Hema',21,75.50)
print("student details:")
s1.display()                  
       