bill=int(input("enter the unit of current"))
if(bill<=100):
    print("the charge is",0)
elif(bill<100 and bill>200):
    print("the charge is 5 ")
else:
    print("the charge is",((bill/100)/2))
