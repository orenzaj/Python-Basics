def packer (name=None, **kwargs):
    print (kwargs)

def unpacker (first_name = None, last_name = None):
    if first_name and last_name:
        print ("Hi, {} {}!".format(first_name, last_name))
    else:
        print ("Hi, no name!")

packer(name = "John", num = 23)
unpacker(**{"last_name": "O", "first_name": "John"})


course_minutes = {"Python Basics": 232, "Django Basics": 237, "Flask Basics": 189, "Java Basics": 133}

for course, minutes in course_minutes.items():
    print ("{} is {} minutes long.".format(course, minutes))
