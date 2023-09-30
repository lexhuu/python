def get_biggest_word(sentence):

  words = sentence.split()
  biggest_word = max(words, key=len)
  return biggest_word

sentence = input("Enter a sentence: ")

number_of_words = get_biggest_word(sentence)

print("The biggest word in the sentence is {} .".format(number_of_words))