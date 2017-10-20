# General search patterns

import re

names_file = open("names.txt")
data = names_file.read()
names_file.close()

#print(re.match(r'Love', data))
#print(re.search(r'Kenneth', data))
#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4]', data))
#print(re.finall(r'\w*, \w+', data))
print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
print(re.findall(r'[trehous]', data, re.IGNORECASE))
#print(re.findall(r'[trehous]', data, re.I))

#print(re.findall(r'''
#    \b@[-\w\d.]*    # First a word boundary , an @, then any number of characters.
#    [^gov\t]+       # Ignore 1 or more instances of the set of letters "gov" and a tab.
#    \b              # Match another word boundary
#''', data, re.VERBOSE|re.I))


#print(re.findall(r"""
#    \b[-\w]*,       # Find a word boundary, 1+ hyphens or characters, and a comma
#    \s              # Find 1 whitespace
#    \[-\w ]+        # Find 1+ hyphens and characters and explicit spaces
#    [^\t\n]         # Ignore tabs and new lines
#""", data, re.X)

line = (re.compile(r'''
    ^(?P<name>[-\w ]*,\s[-\w ]+)\t              # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t           # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t   # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?              # Job and Company
    (?P<twitter>@[\w\d]+)?$                     # Twitter
''', re.X|re.MULTILINE))

print(re.search(line, data).groupdict())
print(line.search(data).groupdict())

for match in line.finditer(data):
    print(match.group('name'))
