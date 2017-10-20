#Write a function named time_machine that takes an integer and a string of "minutes", "hours", "days", or "years".
#This describes a timedelta.
#Return a datetime that is the timedelta's duration from the starter datetime.

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29, 10)

# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)

# Remember: Timedelta + Timedelta will automatically add them up for you
# except years
# Approach: Pack the unit and num in the dictionary
# future = {'minutes': 5}
# warp = datetime.timedelta(**future)
# warp = datetime.timedelta(minutes=5)

def time_machine(num, unit):
    if unit in ("minutes", "hours", "days"):
        add = {unit : num}
    elif unit == "years":
        add = {"days" : num * 365}
    return starter + datetime.timedelta(**add)

print(time_machine(5, "minutes")                                )
#
#    elif time == "hours":
#        if (starter.minute + num) > 23:
#            starter.replace(day =+ 1)
#            starter.minute -= 23
#        return starter.replace(hour = starter.hour + num)
#                                   
#    elif time == "days":
#        return starter.replace(day = starter.day + num)
#                                   
#    elif time == "years":
#        return starter.replace(year = starter.year + num)
