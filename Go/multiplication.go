package main

import (
	"fmt"
	"matrix_basic"
	"cannon"
)



func main(){

	A, err := matrix_basic.Read_matrix_from_file("matrixA")
	if (err != nil){
		fmt.Println("Something went wrong")
	}

	B, err := matrix_basic.Read_matrix_from_file("matrixA")
	if (err != nil){
		fmt.Println("Something went wrong")
	}

	BLOCKS := 3

	submatrix_elements := int(len(A) / BLOCKS)
    ma := cannon.Divide_into_blocks(A, BLOCKS)
    mb := cannon.Divide_into_blocks(B, BLOCKS)

	C := matrix_basic.Initialize_matrix(len(A), len(A[0]))
	
	cannon.Initial_shift_left(ma)
	cannon.Initial_shift_up(mb)

	fmt.Println(C)
/*
	for i := 0; i< len(ma); i++ {
		for j:= 0; j < len(ma[0]); j++ {
			matrix_basic.Multiple_matrixes(ma[i][j], mb[i][j],C, i*submatrix_elements, j*submatrix_elements )
		}
	}*/

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
	fmt.Println(C)
}