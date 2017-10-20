# Create a function named find_words that takes a count and a string. Return a list of all of the words in the string that are count word characters long or longer.

import re


def find_words(count, string):
    return re.findall(r'\w' * count + r'\w*', string)
