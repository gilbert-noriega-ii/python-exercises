#1a)prompt the user for a day of the week, 
#print out whether the day is Monday or not
day = input("What day of the week is it?: ").lower()
if day == "monday":
    print("Looks like you have a case of the Mondays!")
elif day == "sunday":
    print("Thanks goodness it's not Monday")
elif day == "tuesday":
    print("Thanks goodness it's not Monday")
elif day == "wednesday":
    print("Thanks goodness it's not Monday")
elif day == "thursday":
    print("Thanks goodness it's not Monday")
elif day == "friday":
    print("Thanks goodness it's not Monday")
elif day == "saturday":
    print("Thanks goodness it's not Monday")
else:
    print("That's not a day of the week!")

#1b)prompt the user for a day of the week, 
#print out whether the day is a weekday or a weekend
weekday_vs_weekend = input("What day of the week is it?: ").lower()
if weekday_vs_weekend == "saturday":
    print("Yaya it's the weekend!")
elif weekday_vs_weekend == "sunday":
    print("Yaya it's the weekend!")
elif weekday_vs_weekend == "monday":
    print("Don't worry, the weekend will be here sooner than you think!")
elif weekday_vs_weekend == "tuesday":
    print("Don't worry, the weekend will be here sooner than you think!")
elif weekday_vs_weekend == "wednesday":
    print("Don't worry, the weekend will be here sooner than you think!")
elif weekday_vs_weekend == "thursday":
    print("Don't worry, the weekend will be here sooner than you think!")
elif weekday_vs_weekend == "friday":
    print("Don't worry, the weekend will be here sooner than you think!")
else:
    print("That's not a day of the week!")

#1c)create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours
number_of_hours_worked = 43.5
hourly_rate = 23
if number_of_hours_worked > 40:
    paycheck = 40 * hourly_rate + (number_of_hours_worked - 40) * hourly_rate * 1.5
else:
    paycheck = number_of_hours_worked * hourly_rate
print (f"If you worked {number_of_hours_worked} hours at ${hourly_rate} then your paycheck will be ${paycheck}")
