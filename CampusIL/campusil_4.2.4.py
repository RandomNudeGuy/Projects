import calendar

date = input("Enter date: dd/mm/yyyy \n")
date_day = int(date[:-8])
date_month = date[3:-5]
date_year = int(date[6:])

date_month = date_month.replace("0", "")
date_month = int(date_month)


date_weekday = calendar.weekday(date_year, date_month, date_day)

# print(date_month)
# print(date_weekday)

if date_weekday == 0:
    print("Monday")
elif date_weekday == 1:
    print("Tuesday")
elif date_weekday == 2:
    print("Wednesday")
elif date_weekday == 3:
    print("Thursday")
elif date_weekday == 4:
    print("Friday")
elif date_weekday == 5:
    print("Saturday")
elif date_weekday == 6:
    print("Sunday")
else:
    print("Invalid")