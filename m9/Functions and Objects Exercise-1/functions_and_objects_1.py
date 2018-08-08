"""
#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9]
#into [1, 4, 8, 9]
"""

def apply_to_each(List_to_be_modified, function_to_be_applied):
    """
	function check
    """
    for i,j in enumerate(List_to_be_modified):
        List_to_be_modified[i] = function_to_be_applied(List_to_be_modified[i])
    return List_to_be_modified

# def abs(num):
# 	if num < 0:
# 		return num*-1
# 	return num

def main():
	"""main function"""
    data = input()
    data = data.split()
    list1 = []
    for j in data:  
        list1.append(int(j))
    (apply_to_each(list1, abs))
    print (list1)

if __name__ == "__main__":
    main()
