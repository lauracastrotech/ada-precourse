# February 11, 2025
# Programmer: Laura Castro
# Snowman Gameplay

# Constant variable that references the hidden word 
from wonderwords import RandomWord

SNOWMAN_MAX_WRONG_GUESSES = 7
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 8
SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \\( : )/ *',
    '* (_ : _)  ',
    '-----------'
]

def get_letter_from_user(wrong_guesses_list, correct_guesses_list):
    is_correct = False
    user_input_string = None

    while not is_correct:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("Invalid letter please enter a single character")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif user_input_string in wrong_guesses_list or         user_input_string in correct_guesses_list:
            print("You have already guessed that letter!")
        else:
            is_correct = True
        
    return user_input_string

def snowman():
    random_word_generator = RandomWord()
    snowman_word = random_word_generator.word(
        word_min_length = SNOWMAN_MIN_WORD_LENGTH, 
        word_max_length = SNOWMAN_MAX_WORD_LENGTH)
    
    correct_guesses_list = []
    wrong_guesses_list = []

    print(snowman_word)

    while (len(correct_guesses_list) + len(wrong_guesses_list)) < SNOWMAN_MAX_WRONG_GUESSES:
        user_input = get_letter_from_user(wrong_guesses_list, correct_guesses_list)
        if user_input in snowman_word:
            print("You guessed a letter that's in the word!")
            correct_guesses_list.append(user_input)
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
    
        # print_snowman(len(wrong_guesses_list))
        print(f"Wrong guesses: {wrong_guesses_list}")

def print_snowman(wrong_guesses_count):
    for idx in range(SNOWMAN_MAX_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_MAX_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[idx])

# Invoke the function    
snowman()

    
