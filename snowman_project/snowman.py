# February 11, 2025
# Programmer: Laura Castro
# Snowman Gameplay

# Constant variable that references the hidden word 
SNOWMAN_WORD = "broccoli"

def get_letter_from_user():
    user_input_string = input("Guess a letter: ")
    if not user_input_string.isalpha() or len(user_input_string) > 1:
        print("Invalid letter please enter a single character")
    
    return user_input_string

def snowman():
    user_input = get_letter_from_user()
    if user_input in SNOWMAN_WORD:
        print("You guessed a letter that's in the word!")
        return True
    else:
        print(f"The letter {user_input} is not in the word")
        return False

# Invoke the function    
snowman()

    
