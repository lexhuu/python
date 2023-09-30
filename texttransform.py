def capital(string):
  words = string.split()
  capital = []
  for i in words:
    capital_word = i[0].upper() + i[1:]
    capital.append(capital_word)

  capital_string = " ".join(capital)

  return capital_string

str=input("Enter a string")
print(capital(str))