#!/home/resume/test_dir2_VM2/venv/bin/python3


import random

minimum = 1
maximum = 20

answer = random.randint(minimum, maximum)
guess = None
print(f"You will be asked to enter the number from {minimum} to {maximum}.")

while answer != guess:
	guess = int(input(f"Guess the number: "))
	if answer == guess:
		print("Your answer is right!")
	elif guess > answer:
		print("Your number is too high")		
	else:
		print("Your number is too low")
print("Thanks for playing.")
	
