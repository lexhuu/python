class Pairfind:
    def __init__(self,list):
        self.list=list
    def sum1(self):
        self.c=int(len(self.list))
        for i in range(self.c):
            for n in range(i+1,self.c):
                self.sum=self.list[i]+self.list[n]
                if(self.sum==18):
                    print(self.list[i],self.list[n],"is a pair whose sum i 18")
list=[3,8,12.7,6,10,21,15]
obj=Pairfind(list)
obj.sum1()
