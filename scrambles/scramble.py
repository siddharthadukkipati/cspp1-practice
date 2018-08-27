# The 6.00 Word Game
'''Scrabble Program'''
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5,
    'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4,
    'w': 4, 'x': 8, 'y': 4, 'z': 10}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # word_list: list of strings
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for i_i in sequence:
        freq[i_i] = freq.get(i_i, 0) + 1
    return freq

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word_entered, length_v):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    score_word = 0
    for char_acters in word_entered:
        score_word += SCRABBLE_LETTER_VALUES[char_acters]
    if len(word_entered) == length_v:
        return (score_word * len(word_entered)) + 50
    return score_word*len(word_entered)

# Problem #2: Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for _ in range(hand[letter]):
            print(letter, end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def deal_hand(n_n):
    """
    Returns a random hand containing n_n lowercase letters.
    At least n_n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n_n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n_n // 3

    for _ in range(num_vowels):
        x_x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x_x] = hand.get(x_x, 0) + 1

    for _ in range(num_vowels, n_n):
        x_x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x_x] = hand.get(x_x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand_v, word_v):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    temp_dict = hand_v.copy()
    for char_v in word_v:
        temp_dict[char_v] -= 1
    return temp_dict

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    word_dict = get_frequency_dict(word)
    if word not in word_list:
        return False
    for char in word_dict:
        if word_dict.get(char) > hand.get(char,0):
            return False
    return True

#
# Problem #4: Playing a hand
#

def calculate_hand_length(hand_dict):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    sum_num = 0
    for key_var in hand_dict:
        sum_num += hand_dict[key_var]
    return sum_num

def play_hand(hand_v, word_lists, number_v):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      word_lists: list of lowercase strings
      n_n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function;
    #do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score

    # As long as there are still letters left in the hand:

        # Display the hand

        # Ask user for input

        # If the input is a single period:

            # End the game (break out of the loop)

        # Otherwise (the input is not a single period):

            # If the word is not valid:

                # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):

                # Tell the user how many points the word earned, and the updated total score,
                # in one line followed by a blank line

                # Update the hand

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    c_score = 0
    while calculate_hand_length(hand_v):
        display_hand(hand_v)
        input_v = input("Enter a word or insert a '.' to exit: ")
        if input_v == '.':
            print("Your score is: ", c_score)
            break
        elif is_valid_word(input_v, hand_v, word_lists):
            c_score += get_word_score(input_v, number_v)
            print("Your score: ", c_score)
            hand_v = update_hand(hand_v, input_v)
        else:
            print("Enter a valid word")

#
# Problem #5: Playing a game
#

def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    # TO DO ... <-- Remove this comment when you code this function
    #print("play_game not yet implemented.") # <-- Remove this line when you code the function
    while True:
        input_play = input("Enter n to play with new hand\n\
r to play with previous hand\ne to exit: ")
        if input_play == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand, word_list, HAND_SIZE)
        elif input_play == 'r':
            if bool(hand):
                play_hand(hand, word_list, HAND_SIZE)
            else:
                print("Don't enter previous hands. Please re-enter n or e")
        elif input_play == 'e':
            print("End of game!!!")
            break
        else:
            print("You have entered invalid input")
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__': 
    WORDLIST = load_words()
    play_game(WORDLIST)
