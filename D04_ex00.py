#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
import random
def rand_int():
	rand_num = random.randint(1, 25)
	n = 5
	for count in range(n):
		try:
			user_inp = int(input("Guess the number: "))
			if user_inp == rand_num:
				print("Yay! You guessed the number correctly.")
				break
			elif user_inp > rand_num and user_inp <= 25:
				print("Too high")
			elif user_inp < rand_num and user_inp > 0:
				print("Too low")
			else:
				print("Number not in the range of 1 to 25")			
		except:
			print("Nice try, enter a number")
	else:
		print("You are done with your guesses!")

################################################################################
def main():


    rand_int() # Remove this and replace with your function calls
    

if __name__ == '__main__':
    main()