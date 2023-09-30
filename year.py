import re 

s="https://www.hadjhfgsdgf36436nn.2002/06/03.com"
x=re.findall(r'\d\d\d\d/\d+/\d+',s)

print(x)