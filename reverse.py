x=int(input("Enter a number to reverse"))
y=0
while(0<x):
    y=x%10
    x=x//10
    print(y)