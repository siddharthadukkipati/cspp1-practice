'''
    Document Distance - A detailed description is given in the PDF
'''
import math
FILE_NAME = "stopwords.txt"
def similarity(dict_1, dict_2):
    '''
        Compute the document distance as given in the PDF
    '''
    list_1 = ""
    list_2 = ""
    for i in dict_1:
        if i not in '!@#$%^&*()_+-=,.?1234567890':
            if i not in"'":
                list_1 += i
    for i in dict_2:
        if i not in '!@#$%^&*()_+-=,.?1234567890':
            if i not in "'":
                list_2 += i
    list_1 = list_1.split()
    list_2 = list_2.split()
    list_3 = list_1 + list_2
    print(list_3)
    adict = {}
    for word in list_3:
        if word not in load_stopwords(FILE_NAME).keys():
            adict[word] = (list_1.count(word), list_2.count(word))
    numerator, add_1, add_2 = 0, 0, 0
    for a_check in adict:
        numerator += adict[a_check][0]*adict[a_check][1]
        add_1 += adict[a_check][0] ** 2
        add_2 += adict[a_check][1] ** 2
    denominator = math.sqrt(add_1) * math.sqrt(add_2)
    value_check = numerator/denominator
    return value_check

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
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
