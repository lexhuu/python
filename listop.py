list=[2,3,4,5,6]
count= int(len(list))
for i in range(count):
    for n in range(i+1,count):
        sum=list[i]+list[n]
        product=list[i]*list[n]
        if(sum % 2 != 0) and (product % 2 == 0):
            print((list[i],list[n]),"is a pair whose sum is ",sum," odd and product is ",product," even")