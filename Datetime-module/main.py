
#                           OVERVIEW
                 --------------------------------

# Python Datetime module supplies classes to work with date and time. These classes provide a 
# number of functions to deal with dates, times, and time intervals. Date and DateTime are an object in Python, 
# so when you manipulate them, you are actually manipulating objects and not strings or timestamps.
# It can help us figure out the date of the actual day, how to format the date to a particular way, whether a
# date falls on a particular day, etc.


#                           ILLUSTRATION
                 --------------------------------

import datetime as dt              # Since the datetime module has the same name as it's datetime class, it is a
                                   # good idea to always give an alias to the module, so that when using the class
                                   # you can do dt.datetime instead of datetime.datetime

time_now = dt.datetime.now()       # the now method returns the current date and time on the local computer (year, month, day, hour, minute, second, ms)

year = time_now.year
print(year)                                 ----------------->  2023

weekday = time_now.weekday()
print(weekday)                              ----------------->  2  # 2 stands for Wednesday since Python starts counting from Monday as 0

date_of_birth = dt.datetime(year=1995, month=12, day=25)
print(date_of_birth)                        ----------------->  1995-12-25 00:00:00
