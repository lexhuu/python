class bank:
    def __init__ (self, name, acno,bal):
        self.name=name
        self.pin= acno
        self.bal=bal
        
    def deposit(self):
        self.depo=float(input("Enter the amount you want to deposit:"))
        self.bal+=self.depo
        return self.bal
        
    def withdraw(self):
        withd=float(input("Enter the amount you want to withdraw:"))
        if(self.bal>withd):
            self.bal-=withd
            return self.bal
        else:
            print("\nInsufficient balance!")
            exit()


new=[]
while True:
    print ("Enter your choices\n1.Create Account \n2.Show Balance\n3.Deposit Money \n4.Withdraw Money \n5.Exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        name=input("Enter the name of account holder")
        acno=int(input("Enter the pin number of account holder"))
        bal=float(input("Enter the balance of account holder"))
        account=bank(name,acno,bal)
        new.append(account)
        print("Account created sucessfully, Your current balance is",account.bal)
       
    elif ch==2:
        pin=int(input("Enter your pin number"))
        for i in new:
            if i.pin == pin:
                print("Welcome" ,i.name,", Your current bank balance is:",i.bal)
    elif ch==3:
        pin=int(input("Enter your pin number"))
        for i in new:
            if i.pin == pin:
                i.bal = account.deposit()
                print("Deposit successful. Your current account balance is",i.bal)
            else:
                print("You have entered wrong pin number")
                exit()
    
    elif ch==4:
        pin=int(input("Enter your pin number"))
        for i in new:
            if i.pin == pin:
                i.bal = account.withdraw()
                print("Withdrawal successful. Your current account balance is" ,i.bal)
            else:
                print("You have entered wrong pin number")
                exit()
        
    elif ch==5:
        print("Exiting")
        break
    else:
        print("invalid number") 
        break