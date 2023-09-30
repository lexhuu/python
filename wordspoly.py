def count_words(sentence):
    
  words = sentence.split()
  return len(words)

sentence = input("Enter a sentence: ")

number_of_words = count_words(sentence)

print("The sentence contains {} words.".format(number_of_words))