print('Guessing game - try to guess the number from 1 to 100 in 3 guesses!') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)

import random
number=random.randint(1,100)

num_guesses=0
#we_won=0

while num_guesses<3:
    num_guesses+=1
    guess=int(input(f"What is your {num_guesses}. guess? "))
    if guess==number:
        #we_won=1
        break
    elif guess>number:
        print("Your guess is too big.")
    else:
        print("Your guess is too small.")

#if we_won==1:
if guess==number:
    print("You won! Congratulations!")
else:
    print(f"Unlucky! The number was {number}, you lost!")

    