class Romans:

    def __init__(self, number):
        self.number = number


    def ctor(self):
        if self.number == 0:
            return "N"
        elif self.number == 1:
            return "I"
        elif self.number == 2:
            return "II"
        elif self.number == 3:
            return "III"
        elif self.number == 4:
            return "IV"
        elif self.number == 5:
            return "V"
        elif self.number == 6:
            return "VI"
        elif self.number == 7:
            return "VII"
        elif self.number == 8:
            return "VIII"
        elif self.number == 9:
            return "IX"
        elif self.number == 10:
            return "X"
        elif self.number == 11:
            return "XI"
        elif self.number == 12:
            return "XII"
        elif self.number == 13:
            return "XIII"
        elif self.number == 14:
            return "XIV"
        elif self.number == 15:
            return "XV"

        
    def rtoc(self):
        if self.number == "N":
            return "0"
        elif self.number == "I":
            return "1"
        elif self.number == "II":
            return "2"
        elif self.number == "III":
            return "3"
        elif self.number == "IV":
            return "4"
        elif self.number == "V":
            return "5"
        elif self.number == "VI":
            return "6"
        elif self.number =="VII" :
            return "7"
        elif self.number == "VIII":
            return "8"
        elif self.number == "IX":
            return "9"
        elif self.number == "X":
            return "10"
        elif self.number == "XI":
            return "11"
        elif self.number == "XII":
            return "12"
        elif self.number == "XIII":
            return "13"
        elif self.number == "XIV":
            return "14"
        elif self.number == "XV":
            return "15"
        
        
print("Which operation do you want to perform\n1.Integer to Roman\n2.Roman to Integer")
i=int(input("Enter a choice"))  
if i==1:
    num=int(input("enter a number"))
    rom=Romans(num)
    print(num,"is converted into",rom.ctor())
elif i==2:
    num2=input("enter a roman num")
    rom=Romans(num2)
    print(num2,"is converted into",rom.rtoc())
else:
    print("Invalid input")