import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# number guessing game 

secretNumber = random.randint (1,100)
numGuesses = 1
def numFact():
    numFact = ["0! In tennis the word ‘love’ means a score of zero", "1! 1 is significant in fraud detection", "2! Only one prime number is even and it is 2","3! Take any number and multiply it by 3. Now add up the digits of the new number. Whatever number you begin with, the result will always be divisible by 3.", "4! Four colors are sufficient to color any map.", "5! There are only five platonic solids", "6! 6 is the smallest perfect number, meaning it can be made by summing its divisors", "7! According to Christian tradition, there are seven deadly sins", "8! Number 8 is a very lucky number in China, as when said sounds like the word prosper", "9! For 76 years our solar system was said to have nine planets.", "10! Pythagoras and his followers believed 10 was a divine number."]
    return numFact[random.randint(0,len(numFact)-1)]
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
print ("Time for a number fact: " + numFact())
input()