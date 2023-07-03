import calendar
c=calendar.TextCalendar(calendar.SUNDAY)
# print(c)
# str=c.formatmonth(2022,1)
# print(str)

# print("*"*90)
# print("Displaying days of month through calendar")
# for i in c.itermonthdays(2022,1):
#     print(i)

# for name in calendar.month_name:
#     print(name)

# for day in calendar.day_name:
#     print(day)

##PURPOSE: OBTAIN A LIST OF FIRST FRIDAY OF EACH MONTH
print("The meetings will be on :")

for i in range(1,13):
    cal=calendar.monthcalendar(2022,i)
    weekone=cal[0]
    weektwo=cal[1]
    if weekone[calendar.FRIDAY]!=0:
        meetday=weekone[calendar.FRIDAY]
    else:
        meetday=weektwo[calendar.FRIDAY]
    print(calendar.month_name[i],meetday)