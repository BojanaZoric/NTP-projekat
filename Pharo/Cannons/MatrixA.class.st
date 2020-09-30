Class {
	#name : #MatrixA,
	#superclass : #Matrix,
	#category : #Cannons
}

{ #category : #'as yet unclassified' }
MatrixA >> initialShift [ 
"panel canvas addMenu: 'Initial Shift' callback: "

^ [  
	2 to: size do: [ :i|

		1 to: size do:[
			:j| self switchElements: (i-1*size + j) and: 	(i-1*size+1 + (j+i-1-1%size)) 
		]
	 ] .
]
.
]

{ #category : #initialization }
MatrixA >> initialize [ 
	super initialize .
	matrix := super readMatrix: 'matrixA.txt'.
	color:= Color lightBlue .
	^ self
	
]

{ #category : #combining }
MatrixA >> shift [
^
[  
	1 to: size do: [ :i|
		1 to: size-1 do:[
			:j| self switchElements: (i-1*size + j) and: 	(i-1*size + j+1) 
		] 	.
		self switchElements: (i-1*size+size ) and: (i-1*size+1)
	 ] .
]
.

]
