import re
s="hello zendeya ze z900 hii hellzl jsjs"
new=re.findall(r'\b\w*[z]\w*\b',s)

print(new)