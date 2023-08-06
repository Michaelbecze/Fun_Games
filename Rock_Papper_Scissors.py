import random


the_list = ['r', 'p', 's']
computerGuess = random.choice(the_list)
userGuess = input('Select r for Rock, p for Papper, or s for Scissors ')

if userGuess == 'r' and computerGuess == 's' or userGuess == 'p' and computerGuess == 'r' or userGuess == 's' and computerGuess == 'p':
    print(f'You are the winner! The computer guessed {computerGuess}')
elif userGuess == computerGuess:
    print('You Tied')
else:
    print(f'You lost the computer had a {computerGuess}')