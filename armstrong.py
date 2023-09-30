x=int(input("Enter a number"))
rem,sum=0,0
num=x
while num>0:
    rem=num%10
    sum+=(rem*rem*rem)
    num//=10
if sum==x:
    print(x, "is an armstrog number")
else:
    print(x, "is not an armstrong number")
    