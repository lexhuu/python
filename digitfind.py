import re

s="1, 12, 123, 1234, 12345, 123456, 564654515"
x=re.findall("\d{3,}",s)

print(x)