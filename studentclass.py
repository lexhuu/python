class student1:
    def __init__(self, name,rolln,age,mark):
        self.name=name
        self.rolln=rolln
        self.age1=age
        self.mark1=mark
    def display(self):
        print("Name of student is",i.name,"\nRoll number of student is",i.rolln,"\nAge of student is",i.age1,"\nMark of student is",i.mark1)
        
    def age(self):
        self.age1=(input("Enter the age of  student:"))
        return self.age1
    
    def mark(self):
        self.mark1=(input("Enter the mark of  student:"))
        return self.mark1


new=[]
while True:
    print ("Enter your choices\n1.Create student \n2.Show student details\n3.enter student age \n4.enter mark \n5.Exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        name=input("Enter the name of student")
        rolln=int(input("Enter the roll no of the student"))
        age,mark=None,None
        student=student1(name,rolln,age,mark)
        new.append(student)
        print("Name of the registered student is",student.name,"\nRoll number of the registered student is",student.rolln)
    
    elif ch==2:
        pin=int(input("Enter your pin number"))
        for i in new:
            if i.rolln == pin:
                i.display()        
            else:
                print("You have entered wrong pin number")
                exit()
       
    # elif ch==2:
    #     num=int(input("Enter the roll no of the registered student"))
    #     found = False
    #     for i in new:
    #         if i.rolln == num:
    #             i.display()
    #             found = True
                
            # if not found:
            #     print("You have entered wrong roll number")

    elif ch==3:
        pin=int(input("Enter the roll no of the student"))
        for i in new:
            if i.rolln == pin:
                i.age1 = i.age()
                print("The age of the student is succesfully updated")
                i.display()
            else:
                print("You have entered wrong roll number")
    
    elif ch==4:
        pin=int(input("Enter the roll no of the student"))
        for i in new:
            if i.rolln == pin:
                i.mark1 = i.mark()
                print("The mark of the student is succesfully updated")
                i.display()
            else:
                print("You have entered wrong roll number")
        
    elif ch==5:
        print("Exiting")
        break
    else:
        print("invalid number") 
        break