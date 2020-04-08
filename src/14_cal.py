"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]` - 1
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
   Then exit the program. - 2

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

# accepts a possible of 0, 1, 2 args
# [month] and [year]
# functionality : look into datetime module to render two default args with the current month & year if none entered

# case 1: expect that if user enters nothing, the current month's calendar will be printed
# functionality : Render the current month's calender, pass default values into calendar render generating stuff

# case 2: expect that if the user specifies only one argument, assume that this is a month and render the calendar for that month of the current year. Ie. assume current year, assume arg is month
# functionality : render based on month and year as normal, relying on the default year value

# case 3: expect that if the user specifies two args, assume this is month & year args
# functionality : render based on month and year passed in by user

# catch-case: if something breaks, the function should print a statement indicating expected arg format
# things that might break : 
# user input in the wrong format for month or year

import sys
import calendar
from datetime import datetime

# use datetime to get aware data about current month/year
def gimmeCal(month=datetime.today().month, year=datetime.today().year):
    #how do I check if it can be turned into an int before attempting so?
    intYear = int(year)
    intMonth = int(month)

    if(type(intYear) == int and type(intMonth) == int):
        print(calendar.month(intYear, intMonth))
    else:
        print('Inputs could not be converted to integer, double check and re-boot program')

if(len(sys.argv) == 1):
    gimmeCal()
    exit()

if(len(sys.argv) == 2):
    try:
        gimmeCal(month = int(sys.argv[1]))
    except:
        print('Month value cannot be converted to integer')
        exit()

if(len(sys.argv) == 3):
    try:
        int(sys.argv[1])
        try:
            gimmeCal(month = int(sys.argv[1]), year = int(sys.argv[2]))
        except:
            print('Year value cannot be converted to integer')
    except:
        print('Month value cannot be converted to integer')
        exit()