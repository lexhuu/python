def square(list):
    str1=[]
    for i in list:
        squ = int(i)**2
        str1.append(squ)    
    return str1


num = int(input("Enter a number of elements u want to input"))
print("enter",num,"elements in list")
string=[]
for i in range(num):
    element = int(input())
    string.append(element)
result=square(string)
print(result)