"""
#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into
[2, -3, 9, -8]
"""
def apply_to_each(list_to_be_modified, function_to_be_modified):
    """enumerate"""
    for i in range(len(list_to_be_modified)):
        list_to_be_modified[i] = function_to_be_modified(list_to_be_modified[i])
    return list_to_be_modified

def inc_inp(num):
    """increment function"""
    num = num + 1
    return num

def main():
    """function calling"""
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, inc_inp))

if __name__ == "__main__":
    main()
