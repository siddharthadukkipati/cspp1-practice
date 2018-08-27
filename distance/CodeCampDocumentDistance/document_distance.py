'''
    Document Distance - A detailed description is given in the PDF
'''
import math
FILE_NAME = "stopwords.txt"
def similarity(dict_1, dict_2):
    '''
        Compute the document distance as given in the PDF
    '''
    inp_1 = ""
    inp_2 = ""
    for word_s in dict_1:
        if word_s not in '!@#$%^&*()_+-=,.?1234567890':
            if word_s not in"'":
                inp_1 += word_s
    # print(inp_1)
    for word_s in dict_2:
        if word_s not in '!@#$%^&*()_+-=,.?1234567890':
            if word_s not in "'":
                inp_2 += word_s
    # print(inp_2)
    inp_1 = inp_1.split()
    # print(inp_1)
    inp_2 = inp_2.split()
    # print(inp_2)
    list_3 = inp_1 + inp_2
    # print(list_3)
    """combining the 2 list into one and then using
    the count key word to check for the count of that word"""
    a_dict = {}
    for word in list_3:
        if word not in load_stopwords(FILE_NAME).keys():
            a_dict[word] = (inp_1.count(word), inp_2.count(word))
    # print(a_dict)
    numerator, add_1, add_2 = 0, 0, 0
    """for checking the values and calucating the value3"""
    for key_check in a_dict:
        numerator += a_dict[key_check][0]*a_dict[key_check][1]
        add_1 += a_dict[key_check][0] ** 2
        add_2 += a_dict[key_check][1] ** 2
        denominator = math.sqrt(add_1) * math.sqrt(add_2)
    value_check = numerator/denominator
    return value_check
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as file:
        for line in file:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input().lower()
    input2 = input().lower()
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
