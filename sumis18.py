list=[3,8,12,6,10,21,15]
count= int(len(list))
for i in range(count):
    for n in range(i+1,count):
        sum=list[i]+list[n]
        if(sum==18):
            print((list[i],list[n]),"is a pair whose sum is 18")