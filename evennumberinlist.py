list=[]
print("Enter the integer")
while True:
    list1=input()
    if list1:
        list.append(list1)
    else:
        break
    c=[]
    i=0
for i in range(0, len(list)):
    if (int(list[i])%2 == 0):
        c.append(list[i])
print(c)