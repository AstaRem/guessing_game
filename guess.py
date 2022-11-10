#!/home/resume/test_dir2_VM2/venv/bin/python3


import random

minimum = 0
maximum = None
guess = None
counter = 0

print(f"You will be asked to enter the number. There are 4 difficulty levels: Easy: 0-10; Medium: 0-50; Hard: 0-100; Hardcore: 0-1000.")


level_user= input("Please enter a word which level you want to play: ")
level = level_user.lower()

if maximum == None:
	if level == "easy":
		maximum = 10
	elif level == "medium":
		maximum = 50
	elif level == "hard":
		maximum = 100
	elif level == "hardcore":
		maximum = 1000
	else:
		print("please enter a valid option")
		maximum = None
		
answer = random.randint(minimum, maximum)

print(answer, level, maximum)


while answer != guess:
	guess = int(input(f"Guess the number from {minimum} to {maximum}: "))
	counter += 1
	if answer == guess:
		print(f"Your answer is right! It took you {counter} guesses. Thanks for playing!")
	elif guess > answer:
		print("Your number is too high")		
	else:
		print("Your number is too low")

	
