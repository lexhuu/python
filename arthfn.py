def add():
    a=int(input("enter a number")) 
    b= int(input("enter a number")) 
    return (a+b)
def sub():
    a=int(input("enter a number")) 
    b=int(input("enter a number")) 
    return (a-b)
def mult():
    a=int(input("enter a number")) 
    b=int(input("enter a number")) 
    return (a*b)
def div():
    a=int(input("enter a number")) 
    b=int(input("enter a number")) 
    return (a/b)
print ("enter your choices/n 1.Add/n 2.sub/n3.mult/n4.div")  
while True:
    ch=int(input("Enter the choice:"))

    if ch==1:
        print(sum())
    elif ch==2:
        print(sub()) 
    elif ch==3:
        print(mult())
    elif ch==4:
        print(div())
    else:
        print("inavlid number") 
        break
      
                   