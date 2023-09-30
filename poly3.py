s=input("enter a sentence:")
words=s.split()
for word in words:
    if word[0].isupper():
        print(word)