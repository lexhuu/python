def large(str1):
    string = ""
    for strings in str1:
        if len(strings) > len(string):
            string = strings
    return string

def duplicates(str1):
  res = []
  for i in str1:
    if i not in res:
      res.append(i)
  return ''.join(res)


x=["malayalam", "hellboy", "qwefys", "delhi",]
print(duplicates(large(x)))

