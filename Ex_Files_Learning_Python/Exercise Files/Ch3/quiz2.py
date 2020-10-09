# quiz2.py

import calendar
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# Question 1 of 7
# Which code can you use to print a standard, text-formatted monthly calendar for every month in 2020, using Sunday as the first day of the week?
import calendar
cal = calendar.TextCalendar(calendar.SUNDAY)
for m in range(1,13):
    print(cal.formatmonth(2020, m, 0, 0))

# Question 2 of 7
# Given that now=datetime.now(), which call may produce different results on different computers?
now=datetime.now()
print(now.strftime("%c"))

# Question 3 of 7
# Which code will you use to generate a date and time output in the following format?
# 13-Mar-2020 16:42:58
from datetime import datetime
now = datetime.now()
print(now.strftime("%d-%b-%Y %H:%M:%S"))

# Question 4 of 7
# What should come instead of the ??? placeholders for this code to correctly print the number of days until your birthday on Jun 30? Hint: the number of days in a timedelta object can be returned using its days attribute.
# today=date.today()
# bday=date(today.year,6,30)
# diff=???
# if diff>0:
#   print("Birthday in %d days" % diff)
# else:
#   print("Birthday in %d days" % (???))
# answer：
(bday-today).days; diff+365

# Question 5 of 7
# You need to calculate tomorrow's date. Which option should you choose?
# today=date.today()
# # Option A:
# tomorrow=today+timedelta(days=1)
# # Option B:
# tomorrow=date(today.year,today.month,today.day+1)
You are correct!
Option A

# Question 6 of 7
# You create a simple calendar program that needs to print tomorrow's day of the week. Which code will work under all circumstances?
today=date.today()
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("Tomorrow will be "+days[(today.weekday()+1)%7])

# Question 7 of 7
# Which call will return the same result like date.today()?
You are correct!
datetime.date(datetime.now())