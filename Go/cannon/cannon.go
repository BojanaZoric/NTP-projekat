package cannon
/*
import (
	"fmt"
)
*/

func Divide_into_blocks(M [][]int, block_number int)[][][][]int {
	res := make([][][][]int, block_number)
	submatrix_elements := int(len(M)/block_number)

	for i := range res {
		res[i] = make([][][]int, block_number)
		for j := range res[i] {
			res[i][j] = make([][]int, submatrix_elements)
			for k := range res[i][j] {
				res[i][j][k] = make([]int, submatrix_elements)
			}
		}
	}

	for i := range res {
		for j := range res[0] {
			starti := i*submatrix_elements
            endi := (i+1)*submatrix_elements
            startj := j*submatrix_elements
			endj := (j+1)*submatrix_elements
			
			for k := starti; k < endi; k++ {
				for l := startj; l < endj; l++ {
					res[i][j][k-starti][l-startj] = M[k][l]
				}
			}
		}
	}
	return res
}

func Initial_shift_left(A [][][][]int) [][][][]int{
	num_of_rows := len(A)
	num_of_cols := len(A[0])

	for i := 1; i < num_of_rows; i++{
		repeat := i 

		for r := 0; r < repeat; r++ {
			temp := A[i][0]
			j:=0
			for ; j < num_of_cols - 1;j++ {
				A[i][j] = A[i][j + 1]
			}
			A[i][num_of_cols-1] = temp
		}
	}
	return A
}

func Initial_shift_up(B [][][][]int) [][][][]int{
	num_of_rows := len(B)
	num_of_cols := len(B[0])

	for j := 1; j < num_of_cols; j++{
		repeat := j

		for r := 0; r < repeat; r++ {
			temp := B[0][j]
			i:=0
			for ;i < num_of_rows - 1;i++ {
				B[i][j] = B[i+1][j]
			}
			B[num_of_rows-1][j] = temp
		}
	}
	return B
}

func Shift_left(A [][][][]int) [][][][]int{
	num_of_rows := len(A)
	num_of_cols := len(A[0])

	for i := 0; i < num_of_rows; i++{
		temp := A[i][0]
		j:=0
		for ; j < num_of_cols - 1;j++ {
			A[i][j] = A[i][j + 1]
		}
		A[i][num_of_cols-1] = temp
	}
	return A
}

func Shift_up(B [][][][]int) [][][][]int{
	num_of_rows := len(B)
	num_of_cols := len(B[0])

	for j := 0; j < num_of_cols; j++{
			temp := B[0][j]
			i:=0
			for ;i < num_of_rows - 1;i++ {
				B[i][j] = B[i+1][j]
			}
			B[num_of_rows-1][j] = temp
	}
	return B
}