def palin(str):
    
    if(str == str[::-1]):
        for i in range(len(str)):
            print("@",end="" "")
        print("is my mother tongue")
    else:
        print("it is not a palindrome")
        