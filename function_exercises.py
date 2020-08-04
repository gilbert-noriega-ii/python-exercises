#1)Define a function named is_two. 
#It should accept one input and return True
#if the passed input is either the number or the string 2, 
#False otherwise.
def is_two(x):
    if x == 2 or x == '2':
        return True
    else:
        return False

#2)Define a function named is_vowel. 
#It should return True if the passed string is a vowel, 
#False otherwise.
def is_vowel(letter):
    assert type(letter) == str, "Please input a letter as a string"
    if letter.lower() in 'aeiou':
        return True
    else:
        return False

#3)Define a function named is_consonant. 
#It should return True if the passed string is a consonant, 
#False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(letter):
    assert type(letter) == str, "Please input a letter as a string"
    if is_vowel(letter) == True:
        return False
    else:
        return True

#4)Define a function that accepts a string that is a word. 
#The function should capitalize the first letter 
#of the word if the word starts with a consonant.
def capitalize_word(word):
    assert type(word) == str, "Please input a word as a string"
    if word.isdecimal() == True:
        print("Please input a string that does not contain numbers")
    elif is_consonant(word[0]) == True:
        return word.capitalize()
    else:
        print("This function does not capitalize words that start with a vowel")
        return word


#5)Define a function named calculate_tip. 
#It should accept a tip percentage (a number between 0 and 1) 
#and the bill total, and return the amount to tip.
def calculate_tip(tip_percent, bill_total):
    assert type(tip_percent) == float, "Please enter a tip percentage as a float variable"
    assert type(bill_total) == float, "Please enter the bill total as a float variable"
    if tip_percent >= 0 and tip_percent <= 1:
        return bill_total*tip_percent
    else:
        print("Enter the tip percentage as a number between 0 and 1")

#6)Define a function named apply_discount. 
#It should accept a original price, 
#and a discount percentage, 
#and return the price after the discount is applied.
def apply_discount(original_price, discount):
    assert type(original_price) == float, "Please enter original price as a float variable"
    assert type(discount) == float, "Please enter discount as a float variable"
    if discount >= 0 and discount <= 1:
        return original_price - original_price*discount
    else:
        print("Enter the discount as a number between 0 and 1")
        

#Redo number 7


#7Define a function named handle_commas. 
#It should accept a string that is a number 
#that contains commas in it as input, 
#and return a number as output.        
def handle_commas(number):
    assert type(number) == str, "Please enter a string that is a number"
    commas = ","
    if number.isdecimal() == False:
        print("Please enter a string containing only numbers")
    else:
        for char in commas:
            number = number.replace(char,"")
            number = float(number)
        return number

#8)Define a function named get_letter_grade. 
#It should accept a number and 
#return the letter grade associated with that number (A-F).
def get_letter_grade(grade):
    assert type(grade) == float, "Please enter a number as a float variable"
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 75:
        return 'C'
    elif grade >= 70:
        return 'D'
    elif grade >=0:
        return 'F'
    else:
        print("Enter a positive number for your grade")

#9)Define a function named remove_vowels 
#that accepts a string and returns a string 
#with all the vowels removed.
def remove_vowels(word):
    assert type(word) != int and type(word) != float, "Please enter a string"
    vowels = "aeiouAEIOU"
    for char in vowels:
        word = word.replace(char, "")
    return word

#10)Define a function named normalize_name. 
#It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
def normalize_name(name):
    assert type(name) == str, "Please enter a string"
    spaces = " "
    identifiers = "!@#$%^&*-`~=+:;<.,>?/\|][}{"
    for char in name:
        if char in identifiers:
            name = name.replace(char,"")
    name = name.strip()
    name = name.lower()
    for char in spaces:
        name = name.replace(char,"_")
    return name

#11)Write a function named cumulative_sum that accepts 
#a list of numbers and returns a list that 
#is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum(number_list):
    return [sum(number_list[:i+1]) for i in range(len(number_list))]

#Bonus 1A) Create a function named twelveto24. 
#It should accept a string in the format 10:45am or 4:30pm 
#and return a string that is the representation of the time 
#in a 24-hour format. 
def twelveto24(time):
    if time[-2:] == 'am' and time[:2] == '12':
        return '00' + time[2:-2]
    elif time[-2:] == 'am' and (time[:2] == '10' or time[:2] == '11'):
        return time[:-2]
    elif time[-2:] == 'am':
        return '0' + time[:-2]
    elif time[-2:] == 'pm' and time[:2] == '12':
        return time[:-2]
    elif time[-2:] == 'pm' and (time[:2] == '10' or time[:2] == '11'):
        return str(int(time[:2]) + 12) + time[2:-2]
    else:
        return str(int(time[:1]) + 12) + ":" + time[2:-2]

#Bonus 1B) write a function that does the opposite.
def twentyfourto12(time):
    if time[:2] == '00':
        return '12:' + time[-2:] + 'am'
    elif int(time[:2]) < 10:
        return time[1:] + 'am'
    elif int(time[:2]) >=10 and int(time[:2]) <=11:
        return time + 'am'
    elif int(time[:2]) == 12:
        return time + 'pm'
    else:
        return str(int(time[:2]) - 12) + ":" + time[-2:] + 'pm'