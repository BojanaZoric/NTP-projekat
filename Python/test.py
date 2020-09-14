from cannon import *
from time import time
from matrix_basic import read_matrix_from_file

if __name__ == '__main__':

    start = time()

    BLOCKS = 4

    A = read_matrix_from_file('matrixA')

    B = read_matrix_from_file('matrixB')

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

    end = time()
    print("Vreme: ", end-start)