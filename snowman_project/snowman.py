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

def snowman():
    random_word_generator = RandomWord()
    snowman_word = random_word_generator.word(
        word_min_length = SNOWMAN_MIN_WORD_LENGTH, 
        word_max_length = SNOWMAN_MAX_WORD_LENGTH)
    # debug
    print(snowman_word)
    correct_letter_guess_status = build_letter_status_dict(snowman_word)
    wrong_guesses_list = []

    while (len(wrong_guesses_list)) < SNOWMAN_MAX_WRONG_GUESSES:
        user_input = get_letter_from_user(wrong_guesses_list, correct_letter_guess_status)
        
        if user_input in snowman_word:
            correct_letter_guess_status[user_input] = True
            if is_word_guessed(snowman_word, 
                       correct_letter_guess_status):
                print("Congratulations, you win!")
                return
            print("correct letter dict =>",correct_letter_guess_status)
        else:
            wrong_guesses_list.append(user_input)
        print_word_progress_string(snowman_word, correct_letter_guess_status)
        print_snowman(len(wrong_guesses_list))

    # if is_word_guessed(snowman_word, 
    #                    correct_letter_guess_status):
    #     print("Congratulations, you win!")
    print(f"Sorry, you lose! The word was {snowman_word}")

def print_snowman(wrong_guesses_count):
    for idx in range(SNOWMAN_MAX_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_MAX_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[idx])

def get_letter_from_user(wrong_guesses_list,     
                         correct_letter_guess_status):
    is_valid = False
    user_input_string = None

    while not is_valid:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("Invalid letter please enter a single character")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif (user_input_string in correct_letter_guess_status  
              and correct_letter_guess_status[user_input_string]):
            print("You have already guessed that letter and it's in the word!")
        elif user_input_string in correct_letter_guess_status:
            correct_letter_guess_status[user_input_string] = True
            print("You guessed a letter that's in the word!")
        elif user_input_string in wrong_guesses_list: 
            print("You already guessed that letter and it's not in the word!")
        else:
            is_valid = True
        break

    return user_input_string

def build_letter_status_dict(word):
    letter_status_dict = {}
    for letter in word:
        letter_status_dict[letter] = False
    return letter_status_dict

def generate_word_progress_string(snowman_word, correct_letter_guess_status):
    progress_string = ""
    is_not_first_letter = False
    for current_letter in snowman_word:
        if is_not_first_letter:
            progress_string += " "
        if correct_letter_guess_status[current_letter]:
            progress_string += current_letter
        else:
            progress_string += "_"
        is_not_first_letter = True
    return progress_string

def print_word_progress_string(snowman_word, correct_letter_guess_statuses):
    progress_string = generate_word_progress_string(snowman_word, correct_letter_guess_statuses)
    print(progress_string)

def is_word_guessed(snowman_word, correct_letter_guess_statuses):
    for letter in snowman_word:
        if not correct_letter_guess_statuses[letter]:
            return False
    return True

# Invoke the function    
snowman()

    
