from matrix_basic import *
import math
from measure import *

"""
Modul za rad sa matricama prema Cannon-ovom algoritmu
- podela matrice na blokova matrica manjih dimenzija
- preslikavanje blokova na matricu 
- inicijalno pomeranje matrica na levo i na gore (prvi korak u algoritmu)
- pomeranje matrica na gore i na levo (ostali koraci u algoritmu)
"""

@timeit
def divide_into_blocks(matrix, block_number):
    res = [[0 for i in range(block_number)] for j in range(block_number)]
    submatrix_elements = int(len(matrix)/block_number)

    for i in range(block_number):
        for j in range(block_number):
            starti = i*submatrix_elements
            endi = (i+1)*submatrix_elements
            startj = j*submatrix_elements
            endj = (j+1)*submatrix_elements

            res[i][j] = [matrix[k][startj:endj] for k in range(starti, endi)]
    return res


@timeit
def blocks_to_matrix(blocks, matrix):
    n = len(blocks[0])
    m = len(blocks[0][0])

    for i in range(len(blocks)):
        starti = int(i / (math.sqrt(len(blocks))))*n
        startj = int(i % (math.sqrt(len(blocks))))*m
        for j in range(len(blocks[i])):
            for k in range(len(blocks[i][j])):
                matrix[starti+j][startj + k] = blocks[i][j][k]
    return matrix


@timeit
def initial_shift_left(A):
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


@timeit
def initial_shift_up(B):
    #pomeramo drugu matricu na gore, prateci algoritam
    num_of_rows = len(B)
    num_of_cols = len(B[0])
    for j in range(1, num_of_cols):
        repeat = j # za koliko puta se treba pomeriti kolona
        for r in range(repeat):
            # shift column
            temp = B[0][j]
            for i in range(num_of_rows - 1):
                B[i][j] = B[i+1][j]
            B[num_of_rows-1][j] = temp
    return B


@timeit
def shift_left(A):
    num_of_rows = len(A)
    num_of_cols = len(A[0])

    for i in range(0, num_of_rows):
        # shift row
        temp = A[i][0]
        for j in range(num_of_cols - 1):
            A[i][j] = A[i][j + 1]

        A[i][num_of_cols - 1] = temp
    return A


@timeit
def shift_up(B):
    num_of_rows = len(B)
    num_of_cols = len(B[0])
    for j in range(0, num_of_cols):
        # shift column
        temp = B[0][j]
        for i in range(num_of_rows - 1):
            B[i][j] = B[i + 1][j]
        B[num_of_rows - 1][j] = temp
    return B
