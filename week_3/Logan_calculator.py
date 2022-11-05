
"""
================================================================
    Title: Logan_calculator.py
    Author: Carl Logan
    Date: 11/1/2022
    Description: Python Variables and Functions.
================================================================
"""

# add two numbers together
def add(add1, add2) : 
  return add1 + add2

# subtract two numbers
def subtract(subtract1, subtract2) :
  return subtract1 - subtract2

# divide two numbers
def divide(divide1, divide2) :
  return divide1 / divide2

# multiply two numbers
def multiply(multiply1, multiply2) :
  return multiply1 * multiply2

# variables to pass into the functions
num1 = 2
num2 = 11
num3 = 15
num4 = 8

# text with placeholders for the variables, operators and functions
text = '{} {} {} is {}'

# output the text with placeholder values
print(text.format(num1, '+', num3, add(num1, num3)))
print(text.format(num4, '-', num2, subtract(num4, num2)))
print(text.format(num2, '/', num3, round(divide(num2, num3), 2)))
print(text.format(num1, '*', num4, multiply(num1, num4)))
