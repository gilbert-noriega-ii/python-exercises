#1) Import and test 3 of the functions from your functions exercise file.
# Import each function in a different way:
# import the module and refer to the function with the . syntax
import function_exercises
function_exercises.twelveto24('12:30am')

# use from to import the function directly
from function_exercises import is_two
is_two(2)

# use from and give the function a different name
from function_exercises import is_vowel as isv
isv('a')

#For the following exercises, read about and use the itertools module 
#from the standard library to help you solve the problem.
#How many different ways can you combine the letters 
#from "abc" with the numbers 1, 2, and 3?
from itertools import product
print(list(product('abc','123')))
len(list(product('abc','123')))

#How many different ways can you combine 
#two of the letters from "abcd"?
from itertools import combinations as comb
print(list(comb('abcd',2)))
len(list(comb('abcd',2)))

