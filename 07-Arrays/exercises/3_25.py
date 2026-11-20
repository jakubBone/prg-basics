# A program that uses the functions of the module my_text (MyText) for a text.

import my_text

text = "An apple a day keeps the doctor away"

print('Text:', text)
print('Number of words:', my_text.count_words(text))
print('Words from the longest:', ','.join(my_text.words_longest_first(text)))
print('Words ordered alphabetically:', ','.join(my_text.words_alphabetically(text)))
