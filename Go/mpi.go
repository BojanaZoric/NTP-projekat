package main

import (
	"fmt"
	"matrix_basic"
	"cannon"
	"sync"
	"time"
	"math"
	"os"
	"strconv"
)

func ccx(wg *sync.WaitGroup, c chan [][]int, x [][]int, id int){
	defer wg.Done()
	c <- x
	//c <- y
	//fmt.Println(x, id)
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

func process(wg *sync.WaitGroup, process_id int, chanA, chanB []chan [][]int, C *[][]int) {
	
	defer wg.Done()

	BLOCKS := int(math.Sqrt(float64(len(chanA))))
	i := int(process_id / BLOCKS)
	j := int(process_id % BLOCKS)
	var dataA, dataB [][]int
	var ok bool
	
	for r:= 0; r <BLOCKS; r++{
		select {
			// preuzimamo blok matrice A
			case dataA, ok = <-(chanA)[process_id]:
				if ok {
					//fmt.Printf("Value %d was read.%d\n", dataA, process_id)

				} else {
					fmt.Println("Channel closed! Something went wrong")
				}
		}

		select {
			// preuzimamo blok matrice B
			case dataB, ok = <-(chanB)[process_id]:
				if ok {
					//fmt.Printf("Value %d was read.%d\n", dataB, process_id)

				} else {
					fmt.Println("Channel closed! Something went wrong")
			}
		}
		*C, _ = matrix_basic.Multiple_matrixes(dataA, dataB, *C, i*len(dataA),j*len(dataA))
		//fmt.Println(process_id,C)

		select {
			// prosledjujemo sledecem procesu blok matrice A
			case chanA[i * BLOCKS + (j + BLOCKS - 1)%BLOCKS] <- dataA:
		}


		select {
			// prosledjujemo sledecem procesu blok matrice B
			case chanB[((i + BLOCKS - 1) % BLOCKS)*BLOCKS + j] <- dataB:
	}
	}
}

 
func main(){

	start := time.Now()

	temp := os.Args[1]

	PROCESS, err := strconv.Atoi(temp)
	var wg, wg2 sync.WaitGroup

	A, err :=  matrix_basic.Read_matrix_from_file("input/matrixA")
	if (err != nil){
		fmt.Println("Something went wrong")
	}

	B, err := matrix_basic.Read_matrix_from_file("input/matrixB")
	if (err != nil){
		fmt.Println("Something went wrong")
	}

	BLOCKS := int(math.Sqrt(float64(PROCESS)))

	//submatrix_elements := int(len(A) / BLOCKS)
    ma := cannon.Divide_into_blocks(A, BLOCKS)
    mb := cannon.Divide_into_blocks(B, BLOCKS)

	C := matrix_basic.Initialize_matrix(len(A), len(A[0]))
	
	cannon.Initial_shift_left(ma)
	cannon.Initial_shift_up(mb)


	var chansA []chan [][]int
	var chansB []chan [][]int
	for i :=0 ; i< PROCESS;i++ {
		//chansA[i] = make(chan [][]int, 1)
		chansA = append(chansA, make(chan [][]int,1))
		chansB = append(chansB, make(chan [][]int,1))
		//chansB[i] = make(chan [][]int, 1)
		if i < BLOCKS*BLOCKS{
			wg2.Add(1)
			go ccx(&wg2, chansA[i], ma[i/BLOCKS][i%BLOCKS], i)
			wg2.Add(1)
			go ccx(&wg2, chansB[i], mb[i/BLOCKS][i%BLOCKS], i)
		}
	}
	wg2.Wait()
	for r:=0; r<BLOCKS*BLOCKS;r++{
		wg.Add(1)
		go process(&wg, r, chansA, chansB, &C)
	}

	wg.Wait()
	matrix_basic.Write_matrix_to_file("output/parallelOutput", &C)
	fmt.Println("Vreme: ", time.Since(start))
}