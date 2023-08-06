import random

random_number = random.randint(1,10)

guess = 0

while random_number != guess:
    
    guess = int(input("Guess a number between 1 and 10. "))

    if guess > random_number:
        print("That is to high ")
    elif guess < random_number:
        print("That is to low ")

print(f"You guessed the number {random_number} correctly")


