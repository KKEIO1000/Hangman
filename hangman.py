import random

def load_words():
    """
    Returns a list of valid words(lower case) from txt file. 
    """
    print("Loading word list from file...")
    wordlist = open("words.txt", 'r').read().strip().split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list of letters have been guessed so far
    '''
    test = []
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    Returns the secret word where letters not guessed are shown as '_'.
    '''
    test = ''
    for letter in secret_word:
        if letter in letters_guessed:
            test += letter
        else:
            test += '_ '
    return test



def get_available_letters(letters_guessed):
    '''
    Returns the alphabet, exclusing letters that have already been guessed.
    '''
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for letter in letters_guessed:
        alphabet.remove(letter)
    available = ''.join(alphabet)
    return available

def unique_letters(secret_word):
    """
    find the number of unique letters in a word
    """
    unique = []
    for letter in secret_word:
        if letter not in unique:
            unique.append(letter)
    return len(unique)

def match_with_gaps(my_word, other_word):
    no_space = my_word.replace(' ','')
    if len(no_space) == len(other_word.strip()):
        for i in range(len(no_space)):
            if no_space[i] != '_' and no_space[i] != other_word[i]:
                return False
        return True

    return False

def show_possible_matches(my_word):
    '''
    Returns all the available words that could potentially match
    '''
    possible = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word) == True:
            possible.append(other_word)
    if possible:
        for word in possible:
            print(word, end=' ')
    else:
        print('No matches found')


def hangman_with_hints(secret_word):
    '''
    The main loop for the game
    
    1) 6 Total guesses
    2) Each incorrect vowel -2 guesses, each incorrect consonant -1 guess
    3) Invalid input costs 1 of 3 warnings, after warnings are exhausted -1 guess
    4) type '*' to see possible matches
    '''
    remaining_guesses = 6
    letters_guessed = []
    warnings_remaining = 3
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    while remaining_guesses > 0:
        print('\n'+'-'*50)
        print(f'You have {remaining_guesses} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed)}')
        new_letter = str.lower(input('Please guess a letter: '))
        if new_letter == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        elif new_letter in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f'Oops! You\'ve already guessed that letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}')
            else:
                remaining_guesses -= 1
                print(f'Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}')
            continue
        elif len(new_letter) == 1 and str.isalpha(new_letter):
            letters_guessed.append(new_letter)
        else:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f'Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}')
            else:
                remaining_guesses -= 1
                print(f'Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}')
            continue
            
            
        if letters_guessed[-1] in secret_word:
            print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
        else:
            print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')
            if  letters_guessed[-1] in ['a', 'e', 'i', 'o', 'u']:
                remaining_guesses -= 2
            else:
                remaining_guesses -= 1
        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!' \
            '\nYour total score for this game is: ' + str(remaining_guesses + unique_letters(secret_word)))
            break

    if remaining_guesses == 0:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')

secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)