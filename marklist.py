sub1=int(input("Enter mark of first subject"))
sub2=int(input("Enter mark of second subject"))
sub3=int(input("Enter mark of third subject"))
sub4=int(input("Enter mark of fourth subject"))
sub5=int(input("Enter mark of fifth subject"))
sum=sub1+sub2+sub3+sub4+sub5
percentage = (sum*100)/500
print("Total mark =", sum)
print("Average mark =", sum/5)
print("percentage is ", percentage)
if (percentage > 90):
    print("Grade is A+")
elif (percentage > 80):
    print("Grade is A")
elif (percentage > 70):
    print("Grade is B")
elif (percentage > 60):
    print("Grade is C")
else:
    print("Grade is F")