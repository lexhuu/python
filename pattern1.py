n=int(5)
print("*")
for i in range(1, n+1):
    print("*",end="")
    for j in range (1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print("*")
        
for i in range(n-1, 0, -1):
    print("*",end="")
    for j in range (1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print("*")
print("*")

#            *
#            *1*
#            *121*
#            *12321*
#            *1234321*
#            *123454321*
#            *123454321*
#            *1234321*
#            *12321*
#            *121*
#            *1*
#            *

