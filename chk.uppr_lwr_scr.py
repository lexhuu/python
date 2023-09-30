import re

a="hfdfg fdhg SDFH SDKHF hello_nNN_Wo"
match= re.findall(r'[a-z,A-Z,_]+$',a)

print(match)