import re 

s="hi bi chai leatbter ab lofie aoffeb tiffin food chick"
x=re.findall(r'\ba\w*b\b',s)

print(x) 