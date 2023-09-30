tuple=(1,2,3,4,5,7,6,8,9,11,12,13,14,15,16,17,18,19,20,21,22)
a=len(tuple)
i=0
for i in range (a):
    count = 0
    if(tuple[i]==1):
        print(tuple[i], "is either prime nor composite number")
    if(tuple[i]==2 or tuple[i]==3 or tuple[i]==5 or tuple[i]==7 or tuple[i]==11):
        print(tuple[i], "is a prime")
    elif(tuple[i]%2==0 or tuple[i]%3==0 or tuple[i]%5==0 or tuple[i]%7==0 or tuple[i]%11==0):
        count+=1
    if(count >= 1):
        print(tuple[i], "is not a prime")
    else:
        print(tuple[i], "is a prime")