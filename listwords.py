list=[]
count=0
print("Enter the strings")
while True:
    list1=input()
    if list1:
        list.append(list1)
        count+=1
    else:
        break
print(list)    
print(count)
