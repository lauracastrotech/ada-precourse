# Generating random numbers
import random

RANGE_LOW = 0
RANGE_HIGH = 100

def guess_the_number():
    # pick a random number
    random_number = random.randint(RANGE_LOW, RANGE_HIGH)
   
    user_input = get_number_from_user()
    if user_input < RANGE_LOW or user_input > RANGE_HIGH:
        print("Your guess is out of bounds.")
        print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
    elif user_input == random_number:
        print("You guessed the number! Good job!")
    elif user_input > random_number:
        print("Your guess is too high")
    elif user_input < random_number:
        print("Your guess is too low")
    else:
        print("You must input a number!")

def get_number_from_user():
    is_Valid = False
    user_input = None
    while is_Valid != True:
        user_input_string = input("Guess the number: ")
        if user_input_string.isnumeric():
            user_input = int(user_input_string)
            is_Valid = True
        else:
            print("You must input a number!")

    return user_input
# Run the guess_the_number function to test it
guess_the_number()
