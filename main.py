import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
game_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

random_number = int(random.random() * 100 + 1)
print(random_number)


def guessing_game_logic(attempts):
    user_attempts = attempts
    for i in range(1, user_attempts):
        try:
            user_guess = int(input("Make a guess: "))
            if user_guess == random_number:
                print(f"You got it! The answer was {user_guess}")
                exit(0)
            elif user_guess > random_number:
                print("Too high.\nGuess again")
                user_attempts -= 1
                print(f"You have {user_attempts} attempts remaining to guess the number")
            elif user_guess < random_number:
                print("Too low.\nGuess again")
                user_attempts -= 1
                print(f"You have {user_attempts} attempts remaining to guess the number")
            else:
                print("Your input made no sense")
        except ValueError:
            print("Got an input that made no sense")
            user_attempts -= 1
            print(f"You have {user_attempts} attempts remaining to guess the number")


if game_choice == 'easy' or 'e':
    guessing_game_logic(attempts=10)

elif game_choice == 'hard' or 'h':
    guessing_game_logic(attempts=5)
