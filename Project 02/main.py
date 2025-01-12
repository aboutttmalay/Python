# We are going to write a program that generates a random number and asks the user to
# guess it.

# If the player's guess is higher than the actual number, the program displays "Lower
# number please". Similarly, if the user's guess is too IOW, the program prints "higher
# number please" When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.

# Hint: Use the random module.
import random
def guess_number():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number_to_guess:
        guess = int(input("Guess the number: "))
        attempts += 1

        if guess < number_to_guess:
            print("Higher number please")
        elif guess > number_to_guess:
            print("Lower number please")

    print(f"Congratulations! You guessed the number in {attempts} attempts.")

if __name__ == "__main__":
    guess_number()
