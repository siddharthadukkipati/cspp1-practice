"""
defining the matrix multiplication and the matrix addition.
"""
def mult_matrix(matrix_1, matrix_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(matrix_1[0]) != len(matrix_2):
        print("Error: Matrix shapes invalid for mult")
        return None
    # else:
    res_mul = []
    b_str = []
    # rows = len(matrix_1)
    cols = len(matrix_2[0])
    rows_2 = len(matrix_2)
    for i, _ in enumerate(matrix_1):
        # print(i, _)
        for j in range(cols):
            sum_value = 0
            for k in range(rows_2):
                sum_value += (matrix_1[i][k] * matrix_2[k][j])
                k += 1
            b_str.append(sum_value)
            j += 1
        res_mul.append(b_str)
        i += 1
        b_str = []
    return res_mul

def add_matrix(matrix_1, matrix_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(matrix_1) != len(matrix_2) and len(matrix_1[0]) != len(matrix_2[0]):
        print("Error: Matrix shapes invalid for addition")
        return None
    # else:
    add = []
    rows = len(matrix_1)
    for i in range(rows):
        row = []
        for j in range(len(matrix_2[0])):
            row.append(matrix_1[i][j] + matrix_2[i][j])
            j += 1
        add.append(row)
        i += 1
    return add

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    line = input().split(',')
    rows = int(line[0])
    columns = int(line[1])
    matrix = []
    for _ in range(rows):
        line = input().split(" ")
        if len(line) == columns:
            matrix.append([int(j) for j in line])
        else:
            print("Error: Invalid input for the matrix")
            return None
    return matrix

def main():
    """
    calling the funtions and printing the output.
    """
    # read matrix 1
    matrix_1 = read_matrix()

    # read matrix 2
    matrix_2 = read_matrix()

    # print(matrix_1)
    # print(matrix_2)

    # add matrix 1 and matrix 2
    # matrix_sum = add_matrix(matrix_1, matrix_2)
    if (matrix_1 and matrix_2):
        sum_matrix = add_matrix(matrix_1, matrix_2)
        print(sum_matrix)
        print(mult_matrix(matrix_1, matrix_2))
        # print(mult_mat)

    # multiply matrix 1 and matrix 2
    # matrix_mul = mult_matrix(matrix_1, matrix_2)

if __name__ == '__main__':
    main()
