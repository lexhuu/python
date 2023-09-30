def sqr(list):
    sqr_list=[]
    n=len(list)
    for i in range(n):
        square=list[i]**2
        sqr_list.append(square)
    if square>0:
        print("Square of",list,"=",sqr_list)
    else:
        print("Invalid input")
a=int(input("enter a list of numbers"))
l=[]
for i in range(int(a)):
    b=int(input())
    l.append(b)
sqr(l)                    