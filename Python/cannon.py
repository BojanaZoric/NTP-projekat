
def divide_into_blocks(M, block_number):
    res = [[0 for i in range(block_number)] for j in range(block_number)]
    submatrix_elements = int(len(M)/block_number)

    for i in range(block_number):
        for j in range(block_number):
            starti = i*submatrix_elements
            endi = (i+1)*submatrix_elements
            startj = j*submatrix_elements
            endj = (j+1)*submatrix_elements

            res[i][j] = [M[k][startj:endj] for k in range(starti,endi)]
            #print(res[i][j])
    return res


def shift_left(A):
    # pomeramo prvu matricu na levo, prateci algoritam
    # prvi red ne pomeramo, drugi red pomeramo za jedno mesto u levo, treci red pomeramo za dva mesta u levo...
    num_of_rows = len(A)
    num_of_cols = len(A[0])

    for i in range(1, num_of_rows):
        repeat = i # za koliko puta se treba pomeriti red

        for r in range(repeat):
            # shift row
            temp = A[i][0]
            for j in range(num_of_cols - 1):
                A[i][j] = A[i][j+1]

            A[i][num_of_cols-1] = temp
    return A

def shift_up(B):
    #pomeramo drugu matricu na gore, prateci algoritam
    num_of_rows = len(B)
    num_of_cols = len(B[0])
    for j in range(1, num_of_cols):
        repeat = j # za koliko puta se treba pomeriti kolona
        for r in range(repeat):
            print(r, ' ', repeat)
            # shift column
            temp = B[0][j]
            for i in range(num_of_rows - 1):
                B[i][j] = B[i+1][j]
            B[num_of_rows-1][j] = temp
    return B


if __name__ == '__main__':
    A = [[['00'], ['01'], ['02']],
         [['10'], ['11'], ['12'],
         [['20'], ['21'], ['22']]]]

    X = [[12, 7, 3, 3,2,5],
         [4, 5, 6, 3,1,2],
         [7, 8, 9, 4, 3,1],
         [4, 5, 6, 7, 5,3],
         [0, 1, 9, 2, 0, 1],
         [1, 0, 0, 4, 3, 0]]

    mx = divide_into_blocks(X, 3)
    print(shift_up(mx))