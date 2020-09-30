Class {
	#name : #MatrixB,
	#superclass : #Matrix,
	#category : #Cannons
}

{ #category : #'as yet unclassified' }
MatrixB >> initialShift [
	^
[  
	2 to: size do: [ :j|

		1 to: size do:[
			:i| self switchElements: (i-1*size + j) and: 	(i+j-1-1%size*size + (j)) 
				"(i-1*size+1 + (j+i-1-1%size)) "
		]
	 ] .
]
.
]

{ #category : #initialization }
MatrixB >> initialize [ 
	super initialize .
	matrix := super readMatrix: 'matrixB.txt'.
	color:= Color lightRed .
	 ^ self
]

{ #category : #combining }
MatrixB >> shift [
^
[  
	1 to: size do: [ :j|
		1 to: size-1 do:[
			:i| self switchElements: (i-1*size + j) and: 	(i*size + j) 
		] 	.
		self switchElements: (size-1*size + j ) and: (j)
	 ] .
]
.

]
