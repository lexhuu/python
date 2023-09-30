def fib(x):
    n1,n2,sum,count=0,1,0,0
    while(count<x+2):
        print(sum)
        count+=1
        n1=n2
        n2=sum
        sum=n1+n2
        

a=(int(input("enter a number")))
print(fib(a))