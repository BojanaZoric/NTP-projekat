from cannon import *

if __name__ == '__main__':

    BLOCKS = 3

    A = [[12, 7, 3, 3,2,5],
         [4, 5, 6, 3,1,2],
         [7, 8, 9, 4, 3,1],
         [4, 5, 6, 7, 5,3],
         [0, 1, 9, 2, 0, 1],
         [1, 0, 0, 4, 3, 0]]

    B = [[12, 7, 3, 3, 2, 5],
         [4, 5, 6, 3, 1, 2],
         [7, 8, 9, 4, 3, 1],
         [4, 5, 6, 7, 5, 3],
         [0, 1, 9, 2, 0, 1],
         [1, 0, 0, 4, 3, 0]]

    ma = divide_into_blocks(A, BLOCKS)
    mb = divide_into_blocks(B, BLOCKS)

    C = [[0 for i in range(len(A))] for j in range(len(A[0]))]
    submatrix_elements = int(len(A) / BLOCKS)

    ma = initial_shift_left(ma)
    mb = initial_shift_up(mb)

    for i in range(len(ma)):
        for j in range(len(ma[0])):
            multiple_matrixes(ma[i][j], mb[i][j], C, i*submatrix_elements, j*submatrix_elements )


    for repeat in range(BLOCKS - 1):

        ma = shift_left(ma)
        mb = shift_up(mb)
        for i in range(len(ma)):
            for j in range(len(ma[0])):
                multiple_matrixes(ma[i][j], mb[i][j], C, i*submatrix_elements, j*submatrix_elements )

    print_matrix(C)