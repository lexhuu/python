i=0
list=[]
while i<3:
    x=int(input("Enter a number to reverse"))
    list.append(x**2)
    i+=1
    
i=len(list)-1
while 0<=i:
    print(list[i], end=" ")
    i-=1