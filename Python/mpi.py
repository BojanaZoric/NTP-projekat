from mpi4py import MPI
import time
from cannon import *
from math import sqrt
from matrix_basic import read_matrix_from_file

@timeit
def main():
    comm = MPI.COMM_WORLD

    comm.Barrier()
    wt = MPI.Wtime()
    rank = comm.Get_rank()
    size = comm.Get_size()
    processorName = MPI.Get_processor_name()

    BLOCKS = int(sqrt(size))

    for k in range(BLOCKS+1):
        i = int(rank / BLOCKS)
        j = int(rank % BLOCKS)
        if k == 0:
            if rank == 0:
                A = read_matrix_from_file('input/matrixA')

                #B = read_matrix_from_file('input/matrixB')

                SUB_ELEM = int(len(A)/BLOCKS)

                ma = divide_into_blocks(A, BLOCKS)
                #mb = divide_into_blocks(B, BLOCKS)
                ma = initial_shift_left(ma)
                #mb = initial_shift_up(mb)

                for n in range(BLOCKS):
                    for m in range(BLOCKS):
                        if n == 0 and m == 0:
                            continue
                        comm.send(ma[n][m], dest=(n * BLOCKS + m), tag=1)
                        #comm.send(mb[n][m], dest=(n * BLOCKS + m), tag=2)

                dataA = ma[0][0]
                #dataB = mb[0][0]
                dataB = comm.recv(source=1, tag=2)
                C = [[0 for i in range(SUB_ELEM)] for j in range(SUB_ELEM)]
            elif rank == 1:
                B = read_matrix_from_file('input/matrixB')
                SUB_ELEM = int(len(B) / BLOCKS)
                mb = divide_into_blocks(B, BLOCKS)
                mb = initial_shift_up(mb)
                for n in range(BLOCKS):
                    for m in range(BLOCKS):
                        if n == 0 and m == 1:
                            continue
                        comm.send(mb[n][m], dest=(n * BLOCKS + m), tag=2)
                dataB = mb[0][1]
                dataA = comm.recv(source=0, tag=1)
                C = [[0 for i in range(SUB_ELEM)] for j in range(SUB_ELEM)]
            else:
                dataA = comm.recv(source=0, tag=1)
                dataB = comm.recv(source=1, tag=2)
                SUB_ELEM = int(len(dataA))
                C = [[0 for i in range(SUB_ELEM)] for j in range(SUB_ELEM)]

        else:
            # izracunaj
            C = multiple_matrixes(dataA, dataB, C, 0, 0)

            comm.send(dataA, dest=(i * BLOCKS + (j + BLOCKS - 1) % BLOCKS), tag=1)
            comm.send(dataB, dest=(((i+BLOCKS-1) % BLOCKS)*BLOCKS + j), tag=2)

            dataA = comm.recv(source=(i * BLOCKS + (j + 1) % BLOCKS), tag=1)
            dataB = comm.recv(source=(((i + 1) % BLOCKS)*BLOCKS + j), tag=2)

    if rank == 0:
        blocks = [[] for i in range(size)]
        blocks[0] = C
        for i in range(1, size):
            blocks[i] = comm.recv(source=i)

        res = [[0 for i in range(len(A))] for j in range(len(A[0]))]
        res = blocks_to_matrix(blocks, res)
        write_matrix_to_file("output/parallelOutput", res)
    else:
        comm.send(C, dest=0)


    comm.Barrier()

    if rank == 0:
        wt = MPI.Wtime() - wt
        print("Vreme: ", wt)


main()