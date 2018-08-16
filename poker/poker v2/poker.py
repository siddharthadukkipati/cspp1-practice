'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
CARD_VALUES = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    st_list = []
    for i in hand:
        st_list.append(CARD_VALUES[i[0]])
    #print(st_list)
    st_list.sort()
    for i in range(0, len(st_list)-1):
        if st_list[i+1] - st_list[i] != 1:
            return False
    return True



def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    temp = hand[0]
    i = 0
    for i in hand:
        if temp[1] != i[1]:
            return False
    return True
    
def four_of_a_kind(hand):
    '''four of a kind'''
    four_list = []
    for h in hand:
        four_list.append(CARD_VALUES[h[0]])
    four_list.sort()
    for i in range(0, len(four_list)-3):
        if four_list[i] == four_list[i+1] == four_list[i+2] == four_list[i+3]:
            return True
    return False

def three_of_a_kind(hand):
    '''three of kind'''
    three_list = []
    for h in hand:
        three_list.append(CARD_VALUES[h[0]])
    three_list.sort()
    for i in range(0, len(three_list)-2):
        if three_list[i] == three_list[i+1] == three_list[i+2]:
            return True
    return False

def two_pair(hand):
    '''two pairs'''
    two_list = []
    for h in hand:
        two_list.append(CARD_VALUES[h[0]])
    two_list.sort()
    for i in range(0, len(two_list)-3):
        if two_list[i] == two_list[i+1] and two_list[i+2] == two_list[i+3]:
            return True
    return False

def one_pair(hand):
    '''one pair'''
    one_list = []
    for h in hand:
        one_list.append(CARD_VALUES[h[0]])
    one_list.sort()
    for i in range(0,len(one_list)-1):
        if(one_list[i]) == (one_list[i+1]):
            return True
    return False
def full_house(hand):
    '''full house'''
    full_list = []
    for h in hand:
        full_list.append(CARD_VALUES[h[0]])
    full_list.sort()
    for i in range(0, len(full_list)-1):
        if full_list[i] == full_list[i+1] == full_list[i+2] and full_list[i+3] == full_list[i+4]:
            return True
    return False

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    if is_straight(hand) and is_flush(hand):
        return 8
    if four_of_a_kind(hand):
        return 7
    if three_of_a_kind(hand) and one_pair(hand):
        return 6
    if is_flush(hand):
        return 5
    if is_straight(hand):
        return 4
    if three_of_a_kind(hand):
        return 3
    if two_pair(hand):
        return 2
    if one_pair(hand):
        return 1
    return 0

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''


    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
