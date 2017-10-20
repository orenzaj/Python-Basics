# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

def num_teachers(my_teachers):
    return len(my_teachers)

def num_courses(my_teachers):
    total_classes = 0
    for teacher in my_teachers.values():
        total_classes += len(teacher)
    return total_classes

#return a single list of all of the available courses in the dictionary. No teachers, just course names!
def courses(my_teachers):
    course_list = []
    for course in my_teachers.values():
        course_list += (course)
    return course_list

#return the name of the teacher with the most courses. You might need to hold onto some sort of max count variable.
def most_courses(my_teachers):
    max_count = 0
    for teacher, course_count in my_teachers.items():
        if max_count < len(course_count):
            max_count = len(course_count)
            max_teacher = teacher
    return max_teacher

#return a list of lists where the first item in each inner list is the teacher's name and the second item is the number of courses that teacher has.
def stats(my_teachers):
    list_of_stats = []
    for teacher, course in my_teachers.items():
        stats = [teacher, len(course)]
        list_of_stats.append(stats)
    return list_of_stats

teacher_dictionary =  {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections', 'SQL Basics']}
#print(num_teachers(teacher_dictionary))
#print(num_courses(teacher_dictionary))
#print(courses(teacher_dictionary))
#print(most_courses(teacher_dictionary))
print(stats(teacher_dictionary))
