def fn(list1):
    list=[]
    count_a,count_b=0,0
    string=""
    for char in list1:
        if char == 'A':
            count_a+=1
            string+=char
        elif char=='B':
            count_b+=1
            string+=char
            
        if count_a==count_b:
            list.append(string)
            string=""
    return list           
    
str="ABAABBAAABBB"       
print(fn(str))  
