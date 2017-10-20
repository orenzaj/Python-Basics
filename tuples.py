# Create a function named stringcases that takes a single string but returns a tuple of different string formats. The formats should be:
#       All uppercase
#       All lowercase
#       Titlecased (first letter of each word is capitalized)
#       Reversed
# There are str methods for all but the last one.

def stringcases(my_string):
    return (my_string.upper(), my_string.lower(), my_string.title(), my_string[-1::-1])


# Create a function named combo that takes two ordered iterables. These could be tuples, lists, strings, whatever.
# Your function should return a list of tuples.
# Each tuple should hold the first item in each iterable, then the second set, then the third, and so on.
# Assume the iterables will be the same length.
def combo(list_1, list_2):
    my_list = []
    for index, item1 in enumerate(list_1):
        item2 = list_2[index]
        my_list.append((item1, item2))
    return my_list

#print(stringcases("Treehouse"))
#print(combo([1,2,3], 'abc'))
