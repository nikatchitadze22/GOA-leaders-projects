import random

guess_num = random.randint(1, 10)
tries = 5

print("Guess the number from 1 to 10!")
while tries > 0:
    user_guess = int(input(f"You have {tries} tries left. Enter your guess: "))
    tries -= 1
    
    if user_guess == guess_num:
        print(f"Congratulations! You guessed the number. It was {guess_num}.")
        break
    elif tries > 0:
        print("Wrong guess, try again!")
    else:
        print(f"Sorry, you ran out of tries. The correct number was {guess_num}.")
