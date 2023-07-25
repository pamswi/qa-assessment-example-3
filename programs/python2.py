# <QUESTION 1>

# Given a list of items, return a dictionary mapping items to the amount
# of times they appear in the list

# Note: the order of this dictionary does not matter
    
def one(items):

    new_dict = {}

    for item in items:
        count = items.count(item)
        new_dict[item]=count
    return(new_dict)

# <QUESTION 2>

# Given two numbers, a & b, and an operator, evaluate the operation between a & b
# using the given operator

# The operator will be a string, and will only be +, -, *, or /. 

def two(a, b, operator):
    if operator == "+":
        c = a + b
    elif operator == "-":
        c = a - b
    elif operator == "*":
        c = a * b
    elif operator == "/":
        c = a / b
    return c

# <QUESTION 3>

# Given a positive integer, return the next integer below it that has an
# integer square root (is the square of another integer)

# If the number has a square root, just return the number

# <HINT>

# We can use `x ** 0.5` to get the square root of `x`

def three(num):

    sqrt_num= num ** 0.5

    if sqrt_num.is_integer():
        return num
    else:
        y = int(sqrt_num) ** 2
        return y



# <QUESTION 4>

# Given two integers, return the greatest common factor of the two numbers


import math

def four(a, b):
    return math.gcd(a, b)
    

# <QUESTION 5>

# Given a string, return a string where each letter is the previous letter in the alphabet
# in comparison to the original string

# For a or A, use z or Z respectively

# Ignore characters that aren't in the alphabet, such as whitespace or numbers

def five(string):
    reverted_word = ""

    # iterates over each char in a string
    for char in string:
        # checks if char is alphabetic & if upper or lower case
        if char.isalpha():
            is_upper = char.isupper()
            char_lower = char.lower()
            # finds the new value of the ascii alphabet
            ascii_char = ord(char_lower) - 1
            # handles upper and lower case letters
            if char_lower == 'a':
                ascii_char = ord('z')
            if is_upper:
                reverted_word += chr(ascii_char).upper()
            else:
                reverted_word += chr(ascii_char)
        else:
            reverted_word += char

    return reverted_word




# question 1 tests
# print(one(['apple', 'banana', 'orange', 'orange', 'apple', 'apple'])) # → {'apple':3, 'orange':2, 'banana':1}
# print(one(['tic', 'tac', 'toe'])) # → {'tic':1, 'tac':1, 'toe':1}

# question 2 tests
# print(two(2, 4, '+')) # → 6
# print(two(7, 3, '-')) # → 4
# print(two(3, 1.5, '*')) #→ 4.5
# print(two(-5, 2, '/')) # → -2.5

# questions 3 tests
# print(three(7)) #→ 4          # 4 is the square of 2
# print(three(64)) # → 64        # 64 is the square of 8 already
# print(three(32)) # → 25

# question 4 tests
# print(four(32, 24)) # → 8
# print(four(18, 11)) # → 1
# print(four(10, 50)) # → 10

# question 5 tests
print(five('wxyz')) # → 'vwxy'
print(five('abc')) # → 'zab'
print(five('aAbB')) # → 'zZaA'
print(five('hello world')) # → 'gdkkn vnqkc'
print(five('54321')) # → '54321'