import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # function determines if game has been won or keeps going
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
# initialize empty string that will be built out as loop continues
    guessed_word = ''
# checking secret_word letters against letters_guessed 
# ensures that letters are added in the right order
# will also allow a single letter guess to be used multiple times if needed
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            # add space for readability after _
            guessed_word += '_ '
    # strip any trailing or leading whitespace
    return guessed_word.strip()

    


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    # single line check, returns boolean if guess string is found or not
    return guess in secret_word




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    # get the secret word
    secret_word = load_word()
    # initialize empty list
    letters_guessed = []
    # initialize new variable at 0
    incorrect_guesses = 0
    # track incorrect_guesses in relation to max
    max_incorrect_guesses = 0

    # introduce the game
    print("Welcome to Spaceman! Try to guess the secret word.")
    print("You have 7 incorrect guesses allowed")
    # print the blanked out word
    print(get_guessed_word(secret_word, letters_guessed))
    # game logic wrapped in this while loop, keeps going until player wins
    # or max guesses reached
    while incorrect_guesses < max_incorrect_guesses:
        # standardize input to lowercase
        guess = input("Please guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only 1 letter.")
            continue
        if guess in letters_guessed:
            print(f"you already guessed '{guess}.' Try again.")
            continue
# add guess to list
        letters_guessed.append(guess)

        if is_guess_in_word(guess, secret_word):
            print(f"Good guess! {guess} is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
     # show the guessed word so far
        print(get_guessed_word(secret_word, letters_guessed))  
    # check if the game has been won or lost
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you guessed the word!")
            return
    print(f"Sorry, you've run out of guesses. The secret word was '{secret_word}'.")





#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)