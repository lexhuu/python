def deposit_amt(amt):
    depo=float(input("Enter the amount you want to deposit:"))
    amt=amt+depo
    return amt

def withdraw_amt(amt):
    withd=float(input("Enter the amount you want to withdraw:"))
    if(amt>withd):
        amt-=withd
        return amt
    else:
        print("\nInsufficient balance!")
        exit()

amount=float(10000)
while (True):
    
    print("1: Account Balance \n2: Money Deposit \n3: Money Withdrawal \n4: Exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        print("Your current bank balance is:",amount)
    elif(choice==2):
        amount = deposit_amt(amount)
        print("Deposit successful. Your current account balance is",amount)
    elif(choice==3):
        amount = withdraw_amt(amount)
        print("Withdrawal successful. Your current account balance is" ,amount)
    elif(choice==4):
        print("Exiting")
        break
    else:
        print('Invalid Input')
        break