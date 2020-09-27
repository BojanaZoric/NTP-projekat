package matrix_basic

import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"strconv"
)

type MatrixException struct{
	message string
}

func (e MatrixException) Error() string{
	return e.message
}

func Initialize_matrix(n,m int) [][]int {
	C:= make([][]int, n)
	for i := range C {
		C[i] = make([]int, m)
	}
	return C
}

func Multiple_matrixes(x,y, C [][]int, start_i int, start_j int) ([][]int, error) {
	if len(x) == 0 || len(x[0]) == 0 || len(y) == 0 || len(y[0]) == 0{
	 e := MatrixException{
	 	"Matrice moraju imati elemenata"}
	 return nil, e
	}
	
	if len(x[0]) != len(y) {
		e:= MatrixException{
		"Dimenzije se ne poklapaju"}
		
		return nil, e
	}
	
	for i, _ := range x {
		for j, _ := range y[0]{
			for k, _ := range y{
				C[start_i + i][start_j + j] += x[i][k] * y[k][j]
			}
		}
	}
	
	return C, nil
}

func Read_matrix_from_file(filepath string) ([][]int, error){
	file, err := os.Open(filepath)

	if err != nil{
		return nil, err
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	matrix := make([][]int, 0)

    for scanner.Scan() {
		line := scanner.Text()
		tokens := strings.Split(line, " ")
		matrix_row := make([]int,0)
		for _, token := range tokens {
			num, err := strconv.Atoi(token)
			if err != nil {
				return nil, err
			}
			matrix_row = append(matrix_row, num)
		}
		matrix = append(matrix, matrix_row)
    }

    if err := scanner.Err(); err != nil {
        return nil, err
	}
	
	return matrix, nil
}

func Print_matrix(m [][]int) {
	for i:=0;i < len(m); i++ {
		for j:= 0; j < len(m[0]); j++ {
			fmt.Print(m[i][j])
		}
		fmt.Println()
	}
}

func Write_matrix_to_file(filepath string, C *[][]int)error{
	file, err := os.Create(filepath)
    if err != nil {
        return err
    }
    defer file.Close()

    w := bufio.NewWriter(file)
    for i:=0;i < len(*C); i++ {
        fmt.Fprintln(w, strings.Trim(strings.Join(strings.Fields(fmt.Sprint((*C)[i])), " "), "[]"))
    }
    return w.Flush()
}