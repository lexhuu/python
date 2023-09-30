list=[]
print("Enter the integers")
while True:
    list1=input()
    if list1:
        list.append(list1)
    else:
        break
c=list[0]

for i in list:
    if i>c:
        c=i
print(c)        