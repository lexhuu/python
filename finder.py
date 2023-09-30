import re 

s="hi bip chai letter lofie toffee tiffin food chick"
x=re.findall(r'\b[a-z]{3,4}\b',s)

print(x)