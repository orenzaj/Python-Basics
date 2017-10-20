COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}


#Write a function named 'covers' that accepts a single parameter, a set of topics.
#Have the function return a list of courses from COURSES where the supplied set and the course's value (also a set) overlap.
#For example, covers({"Python"}) would return ["Python Basics"].
def covers(my_topics):
    list_of_courses = []

    for course, topics in COURSES.items():
        if my_topics & topics :
            list_of_courses.append(course)
    return list_of_courses
    
#print(covers({"Python"}))


# Create a new function named covers_all that takes a single set as an argument.
# Return the names of all of the courses, in a list, where all of the topics in the supplied set are covered.
# For example, covers_all({"conditions", "input"}) would return ["Python Basics", "Ruby Basics"].
# Java Basics and PHP Basics would be exclude because they don't include both of those topics.

def covers_all(my_topics):
    list_of_courses = []

    for course, topics in COURSES.items():
        if my_topics.issubset(topics):
            list_of_courses.append(course)
    return list_of_courses
