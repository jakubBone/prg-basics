# A module with functions that operate on a text (MyText).
# The file name is in lowercase (my_text), because PEP 8 recommends lowercase names for modules.

def count_words(text):
    # split() cuts the text into a list of words at the spaces
    return len(text.split())


def words_longest_first(text):
    words = text.split()
    # key=len tells sorted() to compare the words by their length; reverse=True gives the descending order
    return sorted(words, key=len, reverse=True)


def words_alphabetically(text):
    words = text.split()
    # key=str.lower ignores the difference between capital and small letters when sorting
    return sorted(words, key=str.lower)
