##importing classes from modules
from datetime import date
from datetime import time
from datetime import datetime

# #getting todays date from today() method of dateclass
# today=date.today()
# print("Today's date is :",today)

# #Printing individual components of date
# print("Date components: ",today.day,today.year,today.month)

# print("Today's weekday number is ",today.weekday())
# days=["Mon","Tues","Wed","Thu","Fri","Sat","Sun"]
# print("which is a ",days[today.weekday()])

## USING FUNCTIONS OF DATETIME CLASS

## now()

# #now() fn of datetime class give us date and time
# today=datetime.now()
# print("The current date and time is \n",today)

# #Getting current time from now
# t=datetime.time(datetime.now())
# print("The current time is : ",t)

##FORMATTING THE TIME OUTPUT

# now=datetime.now()
# print(now.strftime("The current year is %y"))

# print(now.strftime("%Y %B %A ,%d"))

# print(now.strftime("Locale date and time : %c"))

# print(now)

# # %x is used to get locale date
# print(now.strftime("Locale date : %x"))

# #%X is used to obtain local time
# print(now.strftime("Local time is %X"))

# #%I -- to get 12 hour time
# print(now.strftime("Current time(12 hour format) is %I:%M %p"))

# #using %H to get 24 hr time
# print(now.strftime("Current time(24 hr format) is %H:%M"))

##USING TIMEDELTA OBJECTS
##TO use timedelta we need to import timedelta class
from datetime import timedelta

##timedelta is a span or amount of time

print(timedelta(days=365,hours=5,minutes=2))

##using now() to get today's date and time
now=datetime.now()
print(now)

#Printing today's date one year from now
print("One year from now it will be ",now+timedelta(days=365))

##Creating a timedelta that uses more than 1 timedelta argument
print("In two weeks and three days it will be ",str(now+timedelta(days=3,weeks=2)))

#Calculate the date one week ago
t=datetime.now()-timedelta(weeks=1)
print("One week ago it was :",t)