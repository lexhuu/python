import re

x="enter\ngv\nh\n"
new=re.sub(r"\n"," ",x)
print(new)