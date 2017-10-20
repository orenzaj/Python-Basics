def word_count(old_string):
    my_dict = {}
    new_string = old_string.lower().split()

    for word in new_string:
        my_dict[word] = new_string.count(word)
            
    return my_dict

my_string_parameter = "Hello the name is Hello therefore I am John."
print(word_count(my_string_parameter))
