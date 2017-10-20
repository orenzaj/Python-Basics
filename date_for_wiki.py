import datetime

answer_format = '%m/%d'
link_format = '%b_%d'
link = 'https://en.wikipedia.org/wiki/{}'

while True:
    answer = input("What date would you like? Please use the MM/DD format. Enter 'quit' to quit.\n")
    if answer.lower() == 'quit':
        break

    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output + "\n")
    except ValueError:
        print("That's not a valid date. Please try again.")
