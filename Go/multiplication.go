package main

import (
	"fmt"
	"matrix_basic"
	"cannon"
	"os"
	"time"
	"strconv"
)



func main(){
	start := time.Now()

	temp := os.Args[1]
	fmt.Println(temp)
	BLOCKS, err := strconv.Atoi(temp)
	
	if BLOCKS <=0 || err != nil {
		BLOCKS = 2
	}

	A, err := matrix_basic.Read_matrix_from_file("input/matrixA")
	if (err != nil){
		fmt.Println("Something went wrong")
	}

	B, err := matrix_basic.Read_matrix_from_file("input/matrixB")
	if (err != nil){
		fmt.Println("Something went wrong")
	}

	submatrix_elements := int(len(A) / BLOCKS)
    ma := cannon.Divide_into_blocks(A, BLOCKS)
    mb := cannon.Divide_into_blocks(B, BLOCKS)

	C := matrix_basic.Initialize_matrix(len(A), len(A[0]))
	
	cannon.Initial_shift_left(ma)
	cannon.Initial_shift_up(mb)

	//fmt.Println(C)

	for repeat:= 0; repeat < BLOCKS; repeat++ {
		if repeat > 0{ 
			cannon.Shift_left(ma)
			cannon.Shift_up(mb)
		}
		
		for i := 0; i< len(ma); i++ {
			for j:= 0; j < len(ma[0]); j++ {
				 matrix_basic.Multiple_matrixes(ma[i][j], mb[i][j],C, i*submatrix_elements, j*submatrix_elements )
			}
		}
	}
	matrix_basic.Write_matrix_to_file("output/serialOutput", &C)
	fmt.Println("Vreme: ", time.Since(start))
	
}