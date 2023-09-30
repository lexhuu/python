class calc():
    def __init__(self,n,m):
        self.num1 = n
        self.num2 = m
    def Add(self):
        self.sum=self.num1+self.num2
        return self.sum
    def Mul(self):
        self.mult=self.num1*self.num2
        return self.mult
    def div(self):
        self.divi=self.num1/self.num2
        return self.divi
Add1=calc(10,20)
print(Add1.Add())
Add2=calc(22,15)
print(Add2.Mul())  
print(Add1.div())       