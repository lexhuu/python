def character(str,charect):
    count=0
    for char in str:
        if char==charect:
            count+=1
    return count
    
    
string=input("Enter a String")
character1=input("Enter the charecter u want to check")
count=character(string,character1)
print("the charecter",character1,"has",count,"appearences in the string") 