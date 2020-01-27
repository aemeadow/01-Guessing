import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# number guessing game 

secretNumber = random.randint (1,100)
numGuesses = 1
player_name = input("Hello, what is your name?")
print ("Okay, " + str(player_name) + "! I'm thinking of a number between 1 and 100.")
guess = int(input("Enter a guess from 1 to 100!: "))
while (guess != secretNumber): 
    if guess > secretNumber:
        print ("Sorry, the number is less than " + str(guess))
    else:
        print ("Sorry, the number is greater than " + str(guess))
    numGuesses += 1
    guess = int(input("Enter a guess from 1 to 100!:  "))
print ("Right! the number is " + str(secretNumber))
print ("You got it in " + str(numGuesses) + " guesses")
input()