"""
Exercise: Is In
Write a Python function, is_in(char, input_str), that takes in two arguments
a character and String and returns the isIn(char, aStr) which retuns a
boolean value.
This function takes in two arguments character and String and returns one
boolean value.
"""
def is_in(char, input_str):
    """
    char: a single character
    input_str: an alphabetized string
    returns: True if char is in input_str; False otherwise
    """
    # Your code here
    length_inp = len(input_str)
    if length_inp == 0:
        return False
    if input_str[length_inp//2] == char:
        return True
    if input_str[length_inp//2] > char:
        return is_in(char, input_str[0:length_inp//2])
    return is_in(char, input_str[:length_inp-1])

def main():
    """ function calling"""
    data = input()
    data = data.split()
    print(is_in((data[0][0]), data[1]))


if __name__ == "__main__":
    main()
