#!/home/resume/test_dir2_VM2/venv/bin/python3

import random

minimum = 0
maximum = None
guess = None
counter = 0

print(f"You will be asked to enter the number. There are 4 difficulty levels:")
print("a - Easy: 0-10")
print("b - Medium: 0-50")
print("c - Hard: 0-100")
print("d - Hardcore: 0-1000")

while maximum == None:
	level_user= input("Please enter a letter a, b, c or d -  which level you want to play: ")
	level = level_user.lower()
	if level == "a":
		maximum = 10
	elif level == "b":
		maximum = 50
	elif level == "c":
		maximum = 100
	elif level == "d":
		maximum = 1000
	else:
		maximum == None
		level_user= input("Invalid entry. Please press enter.")

answer = random.randint(minimum, maximum)

while answer != guess and maximum != 0:
	guess = int(input(f"Guess the number from {minimum} to {maximum}: "))
	counter += 1
	if answer == guess:
		print(f"Your answer is right! It took you {counter} guesses. Thanks for playing!")
	elif guess > answer:
		print("Your number is too high")		
	else:
		print("Your number is too low")

	
