unit=int(input("enter the unit of current"))
bill=0
if(unit<=100):
    print(unit,"is the charge")
elif(unit>100 and   unit<200):
    bill=((unit-100)*5)+unit
    print(bill," is the charge")
elif(unit>=200):
    bill=((unit-100)*10)+unit
    print(bill," is the charge ")
else:
    print("enter a valid unit of electricity")