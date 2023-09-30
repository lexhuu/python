import re
s="sat , hat , bat , cat , mat , rat"

x=re.findall("[scr]at",s)

print(x)