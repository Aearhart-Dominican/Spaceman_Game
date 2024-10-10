import random

letters = ["a", "b", "c", "d", "e", "f",
           "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "w", "x", "y", "z"]

def get_list_string(list):
    """ 
    Converts a list to a formatted string
    
    Arguments: takes a list

    Returns: a string
    """
    
    list_string = ""
    for item in list:
        list_string += item
    return list_string

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
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter in letters_guessed:
            pass
        else:
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

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    secret_word_display = ""

    for letter in secret_word:
        if letter in letters_guessed:
            secret_word_display += letter
        else:
            secret_word_display += "_"
    
    return secret_word_display
    
def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    for letter in secret_word:
        if letter == guess:
            return True
    
    return False

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''

    letters_guessed = []
    avaliable_letters = letters.copy()
    guesses = 7
    playing = True

    #TODO: show the player information about the game according to the project spec
    print("Welcome To Spaceman!")
    print(f"The secret word contains: {len(secret_word)} letters")
    print("You have 7 incorrect guesses avaliable, please enter one letter per round")
    print("-------------------------")

    while playing:
        
        # Ask the player to guess one letter per round and check that it is only one letter
        valid_letter = False
        while valid_letter == False:
            guessed_letter = input("Enter a Letter: ")
            if guessed_letter in letters_guessed:
                print("That Letter has already been guessed!")
            elif guessed_letter in letters and len(guessed_letter) == 1:
                valid_letter = True
            else:
                print("Invalid input: Only Single Letters Allowed")
        
        avaliable_letters.remove(guessed_letter)

        # Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guessed_letter, secret_word):
            print(f"{guessed_letter} is in the word!")
            letters_guessed.append(guessed_letter)
        else:
            print(f"{guessed_letter} is not in the word")
            letters_guessed.append(guessed_letter)
            guesses -= 1

        # show the guessed word so far
        print(f"Guessed word so far: {get_guessed_word(secret_word, letters_guessed)}")

        # show remaining letters and guesses
        print(f"You have: {guesses} guesses remaining")
        print(f"These letters haven't been guessed yet: {get_list_string(avaliable_letters)}")

        # check if the game has been won or lost
        if guesses < 1:
            print(f"GAME OVER \nThe word was: {secret_word}")
            playing = False
        elif is_word_guessed(secret_word, letters_guessed):
            print(f"YOU WON! \nThe word was: {secret_word}!")
            playing = False
        
        print("-------------------------")

    play_again = input("Play Again? Y/N: ")
    if play_again == "y" or play_again == "Y":
        play_again = True
    else:
        play_again = False
    
    return play_again
        



playing = True

#These function calls that will start the game
while playing:
    secret_word = load_word()
    playing = spaceman(secret_word)