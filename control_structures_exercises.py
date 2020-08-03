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

#2a)While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print (i)
    i += 1

#Create a while loop that will count by 2's starting with 0 and ending at 100.
#Follow each number with a new line.
j = 0
while j <= 100:
    print(j)
    j += 2

#Alter your loop to count backwards by 5's from 100 to -10
j = 0
while j < 100:
    print(j)
    j += 2
while j >= -10:
    print(j)
    j -= 5

#Create a while loop that starts at 2, 
# and displays the number squared on each line 
# while the number is less than 1,000,000
k = 2
while k < 1000000:
    print(k)
    k = k ** 2

#Write a loop that uses print to create the output shown below.
l = 100
while l > 0:
    print(l)
    l -= 5

#2b)For Loops
#Write some code that prompts the user for a number,
#then shows a multiplication table up through 10 for that number.



