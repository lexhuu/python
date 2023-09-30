import re
expression= r'^[a-z+A-Z+0-9+_]{8,}$'
pass1="helowo0098"
match = re.match(expression,pass1)
             
if match:
    print("Valid Password")
else:
    print('Invalid password')