def large(str):
    l2=[]
    for i in range(len(str)):
        a=str[i]
        k=""
        for j in range(0, len(a)):
            if a[j] not in k:
                k+=a[j]
                # print(k)  
            l2.append(k)
        # print(l2)
    t=l2[0]  
    print(len(t))
    for p in range(0, len(l2)):
        if len(t)<=len(l2[p]):
            t=l2[p]
    print(t)
            
x=["malayalam", "hellboys", "qwerty", "delhi", "123654"]
large(x)