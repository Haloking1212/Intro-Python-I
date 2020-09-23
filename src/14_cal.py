"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# print to the user
# ask for the month and the year
# seperate by comma
# create a function that takes the parameters
# print the date

# Telling user to input month and year.
prompt = input("(separated by comma) Enter Month, Year: ")


# cally prints the input month and year of the calendar and todays month and year if no user input.
def cally(parameter):

# today is assigned to datetime.today(), grab_year is assigned to today.year, grab_month is assigned to today.month
# datetime.today takes in two arguments month and year.

    today = datetime.today()
    grab_year = today.year
    grab_month = today.month

# this is a python control flow step 1 prints todays month and year if no user input
#    step 2 prints the accepted prompt input by the user
#    step 3 prints the current year and user input month.

    if not parameter:
        print(calendar.month(grab_year, grab_month))

    elif "," in prompt:
        user_input = [i for i in prompt.split(",")]
        get_month = int(user_input[0])
        get_year = int(user_input[1])
        print(calendar.month(get_year, get_month))

    else:
        grab_month = int(parameter)
        print(calendar.month(grab_year, grab_month))


cally(prompt)



