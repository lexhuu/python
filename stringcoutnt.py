strings= []
print("Enter the string")
while True:
    string = input()
    if string:
        strings.append(string)
    else:
        break
print("length of each string:")
index = 0
while index < len(strings):
    print(len(strings[index]))
    index+=1