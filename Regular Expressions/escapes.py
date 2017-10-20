#Now, write a function named numbers() that takes two arguments: a count as an integer and a string. Return an re.search for exactly count numbers in the string. Remember, you can multiply strings and integers to create your pattern.

#For example: r"\w" * 5 would create r"\w\w\w\w\w".
import re


def first_number(string):
    return re.search(r'\d', string)

def numbers(count, string):
    return re.search(r'\d' * count)
