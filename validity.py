class string:
    def __init__(self, para):
        self.para=para
        
    def check(self):
        # for char in self.para:
            if "(" and ")" or "{" and "}" or "[" and "]" in self.para:
                print ("valid") 
            else:
                print("invalid")
                
n=input("enter the string")
str1=string(n)
n.isalpha()
str1.check()                                        
        
        
        
