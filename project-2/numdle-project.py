import random

def evaluate_guess(guess, correct_sequence):
    feedback = []
    for i in range(4):
        if guess[i] == correct_sequence[i]:
            feedback.append(f"{guess[i]}🟢")
        elif guess[i] in correct_sequence:
            feedback.append(f"{guess[i]}🟡")
        else:
            feedback.append(f"{guess[i]}🔴")
    return feedback

def game():
    print("Hello, let's start gaming.")
    nickname = input("Enter your nickname: ")
    print("The rules are very easy. You must guess the correct order of the numbers.")
    print("If the number is in the correct position, you will see 🟢.")
    print("If the number is in the sequence but in the wrong position, you will see 🟡.")
    print("If the number is not in the sequence, you will see 🔴.")
    print("You have 6 attempts. Let's start.")

    random_4 = [random.randint(0, 9) for i in range(4)]
    random_4_str = ''.join(map(str, random_4))
    max_attempts = 6

    for attempt in range(1, max_attempts + 1):
        guess = input(f"Attempt {attempt}: Enter a 4-digit number: ")

        if len(guess) != 4 or not guess.isdigit():
            print("Your input must be a 4-digit number.")
            continue

        feedback = evaluate_guess(guess, random_4_str)
        print(" ".join(feedback))

        if guess == random_4_str:
            print(f"Congratulations, {nickname}! You guessed the correct sequence!")
            return

    print(f"Sorry, {nickname}, you've used all {max_attempts} attempts. The correct sequence was {random_4_str}.")

game()