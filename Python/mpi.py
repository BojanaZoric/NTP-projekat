from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
processorName = MPI.Get_processor_name()
print('Rank: ', rank)
print('Size: ', size)
print('Name: ', processorName)
