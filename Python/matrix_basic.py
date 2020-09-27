"""
Modul za osnovne operacije sa matricama
- ucitavanje matrice iz fajla
- upis matrice u fajl
- mnozenje matrica
- prikaz matrice
"""


def read_matrix_from_file(file_path):
    with open(file_path, 'r') as f:
        m = [[int(num) for num in line.split(' ')] for line in f]
    return m


def write_matrix_to_file(filepath, matrix):
    with open(filepath, "w") as txt_file:
        for line in matrix:
            txt_file.write(" ".join(map(str, line)) + "\n")  # works with any number of elements in a line


def multiple_matrixes(A, B, C, start_i, start_j):
    if len(A) == 0 or len(A[0]) == 0 or len(B) == 0 or len(B[0]) == 0:
        print('Matrice moraju imati elemenata')
        return
    if len(A[0]) != len(B):
        print('Nisu dobre dimenzije')
        return

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[start_i + i][start_j + j] += A[i][k] * B[k][j]
    return C


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=' ')
        print('')
