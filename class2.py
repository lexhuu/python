class bank:
    def __init__(self,amt):
        self.money = amt
    def deposit_amt(self):
        self.depo=float(input("Enter the amount you want to deposit:"))
        self.money+=self.depo
        return self.money

    def withdraw_amt(self):
        withd=float(input("Enter the amount you want to withdraw:"))
        if(self.money>withd):
            self.money-=withd
            return self.money
        else:
            print("\nInsufficient balance!")
            exit()

person1=bank(float(15000))
person2=bank(float(20000))
person3=bank(float(35000))
while(True):
    print("Select user\n1.User1\n2.User2\n3.User3")
    choice=int(input("Enter your choice:"))
    if choice==1:
        person= person1
    elif choice==2:
        person=person2
    elif choice==3:
        person=person3
        
    while (True):
        print("Enter the operation you want to perform\n1: Account Balance \n2: Money Deposit \n3: Money Withdrawal \n4: Exit")
        choice=int(input("Enter your choice:"))
        if(choice==1):
            print("Your current bank balance is:",person.money)
        elif(choice==2):
            person.money = person.deposit_amt()
            print("Deposit successful. Your current account balance is",person.money)
        elif(choice==3):
            person.money = person.withdraw_amt()
            print("Withdrawal successful. Your current account balance is" ,person.money)
        elif(choice==4):
            print("Exiting")
            break
        else:
            print('Invalid Input')
            break