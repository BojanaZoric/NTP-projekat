# mnozenje matrica
# ucitavanje matrice iz fajla

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

def read_matrix_from_file(file_path):
    with open(file_path, 'r') as f:
        l = [[int(num) for num in line.split(' ')] for line in f]
    return l

def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=' ')
        print('')


if __name__ == '__main__':
    X = [[12, 7, 3,3],
         [4, 5, 6,3],
         [7, 8, 9,4],
         [4,5,6,7]]
    Y = [[5, 8, 1, 2],
         [6, 7, 3, 0],
         [4, 5, 9, 1]]


    print(multiple_matrixes(read_matrix_from_file('matrixA'),read_matrix_from_file('matrixA')))

