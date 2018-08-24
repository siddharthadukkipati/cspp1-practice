import re

def clean(input_value):
    '''
        Make a words list and clean up the words, eliminating all special characters and numbers
    '''
    clean_input = re.compile('[^a-z]')         # cap-'^' mean only, i.e., only a to z
    # print([clean_input.sub('', word.strip()) for word in input_value.lower().split(' ')])
    return [clean_input.sub('', word.strip()) for word in input_value.lower().split(' ')] #returns a list

    # file1_read = list(open(testfile.txt,'r'))
    # file2_read = open('testfile_do.txt','r')
    # file2_read = open('testfile_doing.txt','r')

def word_in_file(input_s, file1, file2, file3):
    clean_input = clean(input_s)
    count1, count2, count3 = 0, 0, 0
    # print(clean_input)
    # print(file1)
    result_dictionary = {}
    # print(result_dictionary)
    for word in clean_input:

        # if word in file1[0]:
        count1 = file1[0].count(word)
            # result_dictionary[word][0] = count1

        # if word in file2[0]:
            # count2 += 1
        count2 = file2[0].count(word)
            # result_dictionary[word][1] = count2
        # if word in file3[0]:
            # count3 += 1
        count3 = file3[0].count(word)
            # result_dictionary[word][2] = count3

        # if word not in result_dictionary:
        #     result_dictionary[word] = (count1, count2, count3)
        result_dictionary[word] = (count1, count2, count3)

    print(result_dictionary)
        


    # print("file1 count:", count1, "file1 count:", count2, "file1 count:", count3)
def load_stopwords(file_name):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = []
    with open(file_name, 'r') as file:
        for line in file:
            stopwords.append(line.split())
    return stopwords


def main():
    input_s = input()
    word_in_file(input_s, file1_read, file2_read, file3_read)
    # clean_input = clean(input_s)
    # print(clean_input)
file1 = 'testfile1.txt'
file2 = 'testfile1_do.txt'
file3 = 'testfile1_doing.txt'
file1_read = load_stopwords(file1)
file2_read = load_stopwords(file2)
file3_read = load_stopwords(file3)

# file1 = 'testfile.txt'
# file2 = 'testfile_do.txt'
# file3 = 'testfile_doing.txt'
main()