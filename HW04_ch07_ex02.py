#!/usr/bin/env python
# HW04_ch07_ex02

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:

#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes
# the resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

###############################################################################
# Imports
import math
# Body
def eval_loop():
	user_inp = ''
	while(True):
		user_inp = input("Enter the expression to be evaluated: ")
		try:
			if user_inp != 'done':
				eval_inp = eval(user_inp)
				print(eval_inp)
			else:
				return eval_inp
		except:
			print("Oops! Please enter a valid expression for evaluation")

###############################################################################
def main():
    eval_loop()

if __name__ == '__main__':
    main()
