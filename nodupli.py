def common(list1,list2):
    list3=[]
    for digit in list1:
        for digit2 in list2:
            if digit==digit2:
                list3.append(digit)
    print(list3)
list1=[1,2,3,4,5]
list2=[4,3,2,6,8]
common(list1,list2)                
            