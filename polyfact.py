def fibo(num):
    n1,n2,sum,count=0,1,0,0
    while(count<num):
        print(sum,end=" ")
        count+=1
        n1=n2
        n2=sum
        sum=n1+n2
