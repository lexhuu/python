fruit=['apple','banana','pear','apricoat','orange']
def alpha(s):
    if s[0] == 'a':
        return s
result=filter(alpha,fruit)
print(list(result))