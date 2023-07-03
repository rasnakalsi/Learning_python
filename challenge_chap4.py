import calendar
day_list=["MONDAY","TUESDAY","WEDNESSDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
day="rasna"

while True:
    print("Which day of the week do yout want to count??")
    day=input("Choose the day: \n 0:Mon,\n1:Tues\n2:Wed\n3:Thu\n4:Fri\n5:Sat\n6:Sun\n or Exit to quit")
    if day.lower()!="exit":
        day=int(day)
    else:
        break
    year=input("Enter year: ")
    year=int(year)
    month=input("Enter month")
    month=int(month)
    
    day_name=day_list[day]
    print("Day name is ",day_name)
    print(day,month,year)

    cal=calendar.monthcalendar(year,month)
    count=0
    for i in range(5):
        if cal[i][day]!=0:
            count=count+1
    
    print("No of ",day_name," in ",month,year," are ",count)
    

print("Exiting program!!")