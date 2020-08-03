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
number = int(input("Choose a number from 1-10: "))
if number > 10 or number < 1:
    print("That is not a number from 1-10!")
else:
    
    print(f"{number} x 1 = {number1}")
    print(f"{number} x 2 = {number * 2}")
    print(f"{number} x 3 = {number * 3}")
    print(f"{number} x 4 = {number * 4}")
    print(f"{number} x 5 = {number * 5}")
    print(f"{number} x 6 = {number * 6}") 
    print(f"{number} x 7 = {number * 7}")
    print(f"{number} x 8 = {number * 8}")
    print(f"{number} x 9 = {number * 9}")      
    print(f"{number} x 10 = {number * 10}")

#Create a for loop that uses print to create the output shown below.
for p in range(10):
    print(str(p) * p)

#2c)Prompt the user for an odd number between 1 and 50. 
#Use a loop and a break statement to continue prompting the user 
#if they enter invalid input. 
#(Hint: use the isdigit method on strings to determine this). 
#Use a loop and the continue statement to output all 
#the odd numbers between 1 and 50, except for the number the user entered.
odd_number = int(input("Choose an odd number between 1 and 50: "))
print(f"Number to skip is: {odd_number} ")
for n in range(50):
    if n == odd_number:
        print(f"Yikes! Skipping number: {odd_number}")
        continue
    elif n % 2 == 1:
        print('Here is an odd number: {}'.format(n))
    elif odd_number > 50 or odd_number < 1:
        print("Invalid Number")
        break

#2d)The input function can be used to prompt for input 
#and use that input in your python code. 
#Prompt the user to enter a positive number and 
#write a loop that counts from 0 to that number. 
#(Hints: first make sure that the value the user entered 
#is a valid number, also note that the input function returns a string, 
#so you'll need to convert this to a numeric type.)
pos_number = int(input("Enter a positive number: "))
w = 0
if pos_number < 0:
    print("This is not a positive number!")
    exit
else:
    while w < pos_number:
        print(w)
        w += 1
#2e)Write a program that prompts the user for a positive integer. 
#Next write a loop that prints out the numbers from the number 
#the user entered down to 1.
pos_int = int(input("Enter a positive number: "))
if pos_int < 0:
    print("This is not a positive number!")
    exit
else:
    while pos_int > 0:
        print(pos_int)
        pos_int -= 1

#3)One of the most common interview questions for entry-level programmers 
#is the FizzBuzz test. Developed by Imran Ghory, the test is designed to 
#test basic looping and conditional logic skills.
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
        continue
    elif n % 5 == 0:
        print("Buzz")
        continue
    elif n % 3 == 0:
        print("Fizz")
        continue
    else:
        print(n)

#4)Display a table of powers.
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.