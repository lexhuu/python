def tri(ch):
    if(ch1==1):
        print("It is an isoceles triangle")
    else:
        print("It is a triangle")

def sq(ch):
    if(ch1==1):
        print("It is Square")
    else:
        print("It is a Rectangle")
print("Enter the number of side shape \n0 sides \n1 side \n2 sides \n3 sides \n4 sides \n5 Exit ")
while True:
    ch=int(input("Enter the choice:"))
   
    if ch==0:
        print("It is a Circle")
    if ch==1:
        print("It is a straight line")
    elif ch==3:
        print("Is the number of sides equal or not \n1.Yes \n2.No")
        ch1=int(input("Enter the choice:"))
        tri(ch1)
    elif ch==4:
        print("Is the number of sides equal or not \n1.Yes \n2.No")
        ch1=int(input("Enter the choice:/"))
        sq(ch1)
    elif ch==5:
        print("Exiting")
        break
    else:
        print("invalid number") 
        break