from mpi4py import MPI
import time
from cannon import *
from math import sqrt
from matrix_basic import read_matrix_from_file



comm = MPI.COMM_WORLD

comm.Barrier()
wt = MPI.Wtime()
rank = comm.Get_rank()
size = comm.Get_size()
processorName = MPI.Get_processor_name()
#print('Rank: ', rank)

#print('Size: ', size)
#print('Name: ', processorName)
BLOCKS = int(sqrt(size))

SUB_ELEM = 32

for k in range(BLOCKS+1):
    i = int(rank / BLOCKS)
    j = int(rank % BLOCKS)
    if k == 0:
        if rank == 0:
            A = read_matrix_from_file('matrixA')

            B = read_matrix_from_file('matrixB')
            ma = divide_into_blocks(A, BLOCKS)
            mb = divide_into_blocks(B, BLOCKS)
            ma = initial_shift_left(ma)
            mb = initial_shift_up(mb)

            for n in range(BLOCKS):
                for m in range(BLOCKS):
                    if(n ==0 and m == 0):
                        continue
                    comm.send(ma[n][m], dest=(n * BLOCKS + m))
                    comm.send(mb[n][m], dest=(n * BLOCKS + m))

            dataA = ma[0][0]
            dataB = mb[0][0]

            C = [[0 for i in range(SUB_ELEM)] for j in range(SUB_ELEM)]
            # izracunaj

        #comm.send(_A, dest=(i*BLOCKS + (j + BLOCKS - 1)%BLOCKS))
        else:
            dataA = comm.recv(source=0)
            dataB = comm.recv(source=0)
            C = [[0 for i in range(SUB_ELEM)] for j in range(SUB_ELEM)]
            #print(dataA)
            #print(dataB)
            #comm.send(dataA, dest=(i * BLOCKS + (j + BLOCKS - 1) % BLOCKS))
            #comm.send(dataB, dest=((i + BLOCKS - 1) % BLOCKS + j))

    else:
        # izracunaj
        C = multiple_matrixes(dataA, dataB, C, 0, 0)

        #print("Rank:",rank, "A primljeno od " ,i * BLOCKS + (j + BLOCKS - 1) % BLOCKS, "B primljeno od ", (((i+BLOCKS-1) % BLOCKS)*BLOCKS + j))
        #print(dataA, ' + ', dataB, ' = ',C)
        comm.send(dataA, dest=(i * BLOCKS + (j + BLOCKS - 1) % BLOCKS))
        comm.send(dataB, dest=(((i+BLOCKS-1) % BLOCKS)*BLOCKS + j))

        #print('sourseA ',(i * BLOCKS + (j + 1) % BLOCKS) )
        #print('sourseB ', (((i + 1) % BLOCKS)*BLOCKS + j))

        dataA = comm.recv(source=(i * BLOCKS + (j + 1) % BLOCKS))
        dataB = comm.recv(source=(((i + 1) % BLOCKS)*BLOCKS + j))


comm.Barrier()
if (rank == 0):
    wt = MPI.Wtime() - wt
    print("Vreme: ", wt)



