x=input("enter the month")
d={30:['april','june','sep','nov'],31:['jan','mar','july','dec','aug'],28:'feb',29:'feb'}
if(x in d[30]):
    print("30 days")
elif(x in d[31]):    
    print("31 days")
elif(x in d[28] or x in d[29]):
    print("28 or 29 days")
else:
    print("enter the correct month")        