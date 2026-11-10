# A program that counts vowels in a text using a while loop instead of a for loop.
# vowels in polish: samogłoski

text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

i = 0
while i < len(text):
    char = text[i]
    # the in operator checks whether a character is inside the string vowels
    if char in vowels:
        vowel_count += 1
    i += 1

print(f"The number of vowels in the text is: {vowel_count}")
