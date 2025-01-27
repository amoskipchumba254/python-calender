# program to display calender of given month of the year
# import module

import calendar

# ask of month and year

yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calender
print(calendar.month(yy, mm))
