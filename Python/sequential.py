from cannon import *
from matrix_basic import read_matrix_from_file
import sys
import math
from measure import timeit


@timeit
def main():
# Block broj blokova u REDU
# Ukupan broj blokova BLOCKS*BLOCKS
    try:
        BLOCKS = math.sqrt(sys.argv[1])
    except:
        BLOCKS = 2

    A = read_matrix_from_file('input/matrixA')

    B = read_matrix_from_file('input/matrixB')

    ma = divide_into_blocks(A, BLOCKS)
    mb = divide_into_blocks(B, BLOCKS)

    C = [[0 for i in range(len(A))] for j in range(len(A[0]))]
    submatrix_elements = int(len(A) / BLOCKS)

    # KORAK 1
    ma = initial_shift_left(ma)
    mb = initial_shift_up(mb)

    for i in range(len(ma)):
        for j in range(len(ma[0])):
            multiple_matrixes(ma[i][j], mb[i][j], C, i*submatrix_elements, j*submatrix_elements)
    # KORACI 2 pa nadalje
    for repeat in range(BLOCKS - 1):
        ma = shift_left(ma)
        mb = shift_up(mb)
        for i in range(len(ma)):
            for j in range(len(ma[0])):
                multiple_matrixes(ma[i][j], mb[i][j], C, i*submatrix_elements, j*submatrix_elements )

    write_matrix_to_file("output/serialOutput", C)


if __name__ == '__main__':
    main()