"""
#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given
testList = [1, -4, 8, -9] into [1, 16, 64, 81]
"""
def apply_to_each(list_to_be_modified, function_to_be_modified):
    """enumerate"""
    for i in enumerate(list_to_be_modified):
        list_to_be_modified[i[0]] = function_to_be_modified(list_to_be_modified[i[0]])
    return list_to_be_modified

def square(num):
    """multiplication function"""
    return num**2

def main():
    """main function"""
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__ == "__main__":
    main()
