package main

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

func multiple_matrixes(x,y [][]int) ([][]int, error) {
	
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
	
	c := make([][]int, len(x))
	for i := range c {
		c[i] = make([]int, len(x[0]))
	}
	
	for i, _ := range x {
		for j, _ := range y[0]{
			for k, _ := range y{
				c[i][j] += x[i][k] * y[k][j]
			}
			
		}
	}
	
	return c, nil
}

func read_matrix_from_file(filepath string) ([][]int, error){
	file, err := os.Open(filepath)

	if err != nil{
		return nil, err
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	matrix := make([][]int, 0)

    for scanner.Scan() {
		// fmt.Println(scanner.Text())
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

func main(){

	a, err := read_matrix_from_file("matrixA")
	if (err != nil){
		fmt.Println("Something went wrong")
	}
	b, err := read_matrix_from_file("matrixA")
	if (err != nil){
		fmt.Println("Something went wrong")
	}
	fmt.Println(multiple_matrixes(a,b))
	
}