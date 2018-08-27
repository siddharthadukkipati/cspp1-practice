'''program for checking various conditions in game'''
def tic_tac_toe(matrix_inp):
    '''function for playing Tictactoe game'''
    result_matrix = []
    for i in range(0, 3):
        if matrix_inp[i][0] == matrix_inp[i][1] == matrix_inp[i][2]:
            result_matrix.append(matrix_inp[i][0])
    for i in range(0, 3):
        if matrix_inp[0][i] == matrix_inp[1][i] == matrix_inp[2][i]:
            result_matrix.append(matrix_inp[0][i])
    if matrix_inp[0][0] == matrix_inp[1][1] == matrix_inp[2][2]:
        result_matrix.append(matrix_inp[0][0])
    if matrix_inp[2][0] == matrix_inp[1][1] == matrix_inp[0][2]:
        result_matrix.append(matrix_inp[0][2])
    if result_matrix == []:
        print('draw')
        return None
    if len(result_matrix) == 1:
        if result_matrix[0] == 'x' or result_matrix[0] == 'o':
            print(result_matrix[0])
        else:
            print("invalid input")
        return result_matrix[0]
    else:
        print("invalid game")
        return None
def main():
    '''main function '''
    matrix_inp = []
    for _ in range(0, 3):
        matrix_inp.append(input().split())
    tic_tac_toe(matrix_inp)
if __name__ == '__main__':
    main()
