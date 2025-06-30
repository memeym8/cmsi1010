import random

random_number = random.randint(1, 1000)
print(random_number)


def get_guess():
    guess = input(
        "Guess a number between 1 and 1000.  You can type bye or exit to quit the program\n"
    )
    if not guess.isnumeric():
        print("Please enter a valid number")
        return get_guess()
    guess = int()
    if guess > random_number:
        print("Too high")
        return get_guess()
    if guess < random_number:
        print("Too low")
        return get_guess()
    if guess == random_number:
        print("Congratulations!  You guessed the number!")
        return


get_guess()
