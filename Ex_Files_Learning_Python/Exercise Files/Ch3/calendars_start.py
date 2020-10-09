#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
# Sunday is the day I want to start the date on:
c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2020,10,0,0)
# print(st)

# create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2020,10)
# print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2020,10):
#     print(i) #0 are days belong to another month
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meeting will be on: ")
for m in range(1,13):
    cal = calendar.monthcalendar(2020,m)
    # print(cal) ##cal is a list of weeks
    weekone=cal[0]
    # print(weekone)
    weektwo=cal[1]

    if weekone[calendar.FRIDAY]!=0:
        meetday=weekone[calendar.FRIDAY]
    else:
        meetday=weektwo[calendar.FRIDAY]
    print("%10s %2d" %(calendar.month_name[m],meetday))
    #%s acts a placeholder for a string while %d acts as a placeholder for a number
    # %2d will print the parameter right aligned as int with at least 2 characters