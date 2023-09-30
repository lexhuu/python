def calc():
    dict={"T-Shirt":350,"Shirt":450,"Jeans":150,"pants":160}
    item1={}
    total=0
    while True:
        print("\nAvailable items")
        for items,price in dict.items():
            print(f"{items}:{price}")
            
        num=int(input("\n Enter the number of items you want to select"))
        if num ==0:
            break
        if num > len(dict):
            print("Error: you cannot select more items than available")
            continue
        sort=sorted(dict.items())
        for item, price in sort[:num]:
            item1[item]=price
            total+=price
    print("Selected items:")
    for item, price in item1.items():
        print(f"{item}:{price}")
    print("total price:",total)
    
calc()
    
# print("Enter your choices\n1.T-Shirt \n2.Shirt \n3.Jeans \n4.Pants \n5.Exit")
# item=[]
# while True:
#     ch=int(input("Enter the choice:"))
   
#     if ch==1:
        
#         print(calc(item))
#     elif ch==2:
#         item=dict["Shirt"]
#         print(calc(item)) 
#     elif ch==3:
#         item=dict["Jeans"]
#         print(calc(item))
#     elif ch==4:
#         item=dict["Pants"]
#         print(calc(item))
#     elif ch==5:
#         print("Exiting")
#         break
#     else:
#         print("invalid number") 
#         break
# print("Your current choices are:",item)