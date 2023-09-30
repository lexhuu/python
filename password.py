print("Enter your password")

import re
password=input("")
if(bool(re.match('^[a-zA-Z0-9]*$',password))==True):
    print("invalid")
elif len(password) >= 8:
    print("valid")
else:
     print("invalid")