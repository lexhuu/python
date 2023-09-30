class InvalidRange(Exception):
    pass

try:
    marks= input("Enter marks")
    marks=int(marks)
    if (marks < 0 or marks > 100):
            raise InvalidRange
    print("Marks",marks)
        
except ValueError:
    print("Invalid input")
except InvalidRange:
    print("Input value out of range")