i=int(input("enter number of lines"))
j=1
while j<=i:
    k=i
    l=1
    while l<=j:
        print(end=" ")
        l+=1
    while k>=j:
        print("*", end=" ")
        k-=1
    print()
    j+=1 