#1) Import and test 3 of the functions from your functions exercise file.
# Import each function in a different way:
# import the module and refer to the function with the . syntax
import function_exercises  #importing function_exercises file
function_exercises.twelveto24('12:30am') #running twelveto24 function

# use from to import the function directly
from function_exercises import is_two #importing is_two function
is_two(2)  #running is_two function 

# use from and give the function a different name
from function_exercises import is_vowel as isv #importing is_vowel function renamed as isv
isv('a')  #running is_vowel function

#For the following exercises, read about and use the itertools module 
#from the standard library to help you solve the problem.
#How many different ways can you combine the letters 
#from "abc" with the numbers 1, 2, and 3?
from itertools import product  #from itertools library, import product function
print(list(product('abc','123'))) #print the list of combinations for 'abc' and '123'
len(list(product('abc','123')))  #give the amount of combinations for 'abc' and '123'

#How many different ways can you combine 
#two of the letters from "abcd"?
from itertools import combinations as comb #from itertools library, import combinations function as comb
print(list(comb('abcd',2))) #print the list of 2 different letter combinations for 'abcd'
len(list(comb('abcd',2))) #give the amount of 2 different letter combinations for 'abcd'

#Use the load function from the json module to open this file, 
#it will produce a list of dictionaries. 
#Using this data, write some code that calculates and 
#outputs the following information:
import json # importing json and all modules
prof = open('profiles.json') # storing the open json file command as variable prof
data = json.load(prof) #storing the loading of json file command as variable data

#Total number of users
number_of_users = len([profile['_id'] for profile in data]) #counting number of profiles in dictionary called data
print(f'The total number of users is {number_of_users}.') #printing results

#Number of active users
number_of_active_users = len([profile['isActive'] for profile in data if profile['isActive'] == True]) ##counting number of profiles in dictionary called data if isActive equals true
print(f'The total number of active users is {number_of_active_users}.') # print our results

#Number of inactive users
number_of_inactive_users = len([profile['isActive'] for profile in data if profile['isActive'] == False]) ##counting number of profiles in dictionary called data if isActive equals true
print(f'The total number of active users is {number_of_inactive_users}.') # print our results

#Grand total of balances for all users
total_balance = 0
for profile in data:       
    total_balance += float(profile['balance'].replace(",", '').replace("$", "")) 
print(f'The grand total of balances for all user is ${round(total_balance, 2)}.')

#Average balance per user
total_average = round(total_balance / number_of_users, 2)
print(f'The overall average balance per user is ${total_average}.')

#User with the lowest balance
lowest_balance = [profile['name'] for profile in data if profile['balance'] == min([profile['balance'] for profile in data])] 
print(f"The user with the lowest balance is {lowest_balance[0]}.")

#User with the highest balance
highest_balance = [profile['name'] for profile in data if profile['balance'] == max([profile['balance'] for profile in data])] 
print(f"The user with the highest balance is {highest_balance[0]}.")

#Most common favorite fruit
favorite_fruits = [profile['favoriteFruit'] for profile in data]
fruit_counts = {}
for fruit in favorite_fruits:
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1
print(f"The most common favorite fruit is {max(fruit_counts)}.")

#Least most common favorite fruit
print(f"The least common favorite fruit is {min(fruit_counts)}.")

#Total number of unread messages for all users
unread_messages = [int(profile['greeting'].lower().strip("abcdefghijklmonpqrstuvwxyz!,. ")) for profile in data if 'unread' in profile['greeting']]
total_messages = sum(unread_messages) 
print(f'There are {total_messages} unread messages for all users.')