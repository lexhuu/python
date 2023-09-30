try:
    num= int(input("Enter numerator"))
    den= int(input("Enter denominator"))
    try:
        res=num/den
        print (res)
    except:
        print("Exception handled")
except:
     print("invalid input")
print("End of prgrm")