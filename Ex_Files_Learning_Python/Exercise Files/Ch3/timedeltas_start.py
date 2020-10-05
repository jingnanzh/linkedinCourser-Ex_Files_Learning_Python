#
# Example file for working with timedelta objects
#
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=365,hours=5,minutes=1))

# print today's date
now  = datetime.now()

print('today is:'+ str(now))
#
# # print today's date one year from now
print('one year from now will be:' + str(now+timedelta(days=365)))
#
# # create a timedelta that uses more than one argument
print('in 2 days and 3 weeks, it will be:' + str(now+timedelta(days = 2, weeks = 3)))

# calculate the date 1 week ago, formatted as a string
t = now  - timedelta(weeks = 1)
s = t.strftime('%A %B %d, %Y')
print('one week ago it was:' + s)

### How many days until April Fools' Day?
today = date.today()
print(today)
afd = date(today.year, 4, 1)
lisa_birthday = date(2005,3, 19)
print("lisa_birthday is ",lisa_birthday)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April fool's day alreay went by %d days ago" % ((today - afd).days))
    afd = afd.replace(year = today.year+1)
    # lisa_birthday = lisa_birthday.replace(year=today.year+1)

# Now calculate the amount of time until April Fool's Day  
time_to_afd = afd - today
print("it's just" , time_to_afd, "days to April fool's day" )
time_to_lisa_birthday = today- lisa_birthday
print("it's just" , time_to_lisa_birthday, "days to Lisa's birthday" )
days_lisa = today - lisa_birthday
print("史文琦 has been with mom for ", days_lisa)

