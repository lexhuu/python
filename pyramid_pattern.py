i=5
j=1
while j<=i:
    k=1
    l=i
    while l>=j:
        print(end=" ")
        l-=1
    while k<=j:
        print("*", end=" ")
        k+=1
    print()
    j+=1 