import random
print ("Hello warrior. Enter your name and face death standing proud")
name = input(str)
secretNumber= random.randint(1,99)
print ("HAHAHA," + name + ", i am hiding somewhere between 1 and 99! TRY AND FIND ME BEFORE I KILL YOUR ENTIRE VILAGE")

for guessesTaken in range(1, 20):
	print ("Roll the D20 until you hit that fatal 1")
	guess = int(input())
	if guess < secretNumber:
		print ("YOU SWUNG TOO LOW!")
		print ("I SHALL ATTACK YOUR TZONE!")
	elif guess > secretNumber:
		print ("YOU SWING TOO HIGH!")
		print ("YOUR LEGS ARE MINE, " + name)
	else:
		break #unless the answer is divisible by zero!!
		
if guess == secretNumber:
	print ("GAH! I AM SLAIN! FOUL HERO I SHALL RISE AGAIN!")
else:
	print ("FOOL I HAVE WON!")
	print ("DARE YOU CHALLENGE ME AGAIN IN THE NEXT LIFE?")
