package main

import (
	"fmt"
	"matrix_basic"
	"cannon"
	"sync"
)

func ccx(wg *sync.WaitGroup, c chan [][]int, x [][]int, id int){
	defer wg.Done()
	c <- x
	//c <- y
	fmt.Println(x, id)
}

func ccc(c chan [][]int, n int){
	var x, y [][]int
	select {
		case x = <-c:
			select {
			case y = <-c:
				fmt.Println("YES")
			}
		default:
			fmt.Println("NO")
	}
	
	
	fmt.Println(n,x, y)
}

func process(wg *sync.WaitGroup, process_id int, chanA, chanB [9]chan [][]int, C *[][]int) {
	
	defer wg.Done()

	BLOCKS := 3
	i := int(process_id / BLOCKS)
	j := int(process_id % BLOCKS)
	//fmt.Println("HI ", process_id)
	var dataA, dataB [][]int
	var ok bool
	
	for r:= 0; r <BLOCKS; r++{
		fmt.Println("Iteracija ", r)
		select {
			case dataA, ok = <-(chanA)[process_id]:
				if ok {
					fmt.Printf("Value %d was read.%d\n", dataA, process_id)

				} else {
					fmt.Println("Channel closed!")
				}
		}

		select {
			case dataB, ok = <-(chanB)[process_id]:
				if ok {
					fmt.Printf("Value %d was read.%d\n", dataB, process_id)

				} else {
					fmt.Println("Channel closed!")
			}
		}
		*C, _ = matrix_basic.Multiple_matrixes(dataA, dataB, *C, i*2,j*2)
		//fmt.Println(process_id,C)

		select {
			case chanA[i * BLOCKS + (j + BLOCKS - 1)%BLOCKS] <- dataA:
				fmt.Println("Upisamp ", process_id, " A u ", (i * BLOCKS + (j + BLOCKS - 1)%BLOCKS))
		}


		select {
			case chanB[((i + BLOCKS - 1) % BLOCKS)*BLOCKS + j] <- dataB:
				fmt.Println("Upisamp "," B u ", ((i + BLOCKS - 1) % BLOCKS)*BLOCKS + j)
	}
	}
}

func main(){

	var wg, wg2 sync.WaitGroup

	A, err := matrix_basic.Read_matrix_from_file("matrixA")
	if (err != nil){
		fmt.Println("Something went wrong")
	}

	B, err := matrix_basic.Read_matrix_from_file("matrixA")
	if (err != nil){
		fmt.Println("Something went wrong")
	}

	BLOCKS := 3

	//submatrix_elements := int(len(A) / BLOCKS)
    ma := cannon.Divide_into_blocks(A, BLOCKS)
    mb := cannon.Divide_into_blocks(B, BLOCKS)

	C := matrix_basic.Initialize_matrix(len(A), len(A[0]))
	
	cannon.Initial_shift_left(ma)
	cannon.Initial_shift_up(mb)

	fmt.Println(C)

	var chansA [9]chan [][]int
	var chansB [9]chan [][]int
	for i := range chansA {
		chansA[i] = make(chan [][]int, 1)
		chansB[i] = make(chan [][]int, 1)
		if i < BLOCKS*BLOCKS{
			wg2.Add(1)
			go ccx(&wg2, chansA[i], ma[i/BLOCKS][i%BLOCKS], i)
			wg2.Add(1)
			go ccx(&wg2, chansB[i], mb[i/BLOCKS][i%BLOCKS], i)
		}
	}
	wg2.Wait()
	fmt.Println("**************************")
	for r:=0; r<BLOCKS*BLOCKS;r++{
		wg.Add(1)
		go process(&wg, r, chansA, chansB, &C)
	}

	wg.Wait()
	fmt.Println("Konacno: " , C)
}