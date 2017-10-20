# Create a function named find_emails that takes a string. Return a list of all of the email addresses in the string.

def find_emails(string):
    return re.findall(r'[+\w\d.-]+@[+\w\d.-]+', string)
