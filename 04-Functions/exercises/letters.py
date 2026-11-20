# A module with a function that counts how many times a letter appears in a text.

def count_letter(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    return count
