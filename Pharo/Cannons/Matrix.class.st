Class {
	#name : #Matrix,
	#superclass : #Object,
	#instVars : [
		'elements',
		'panel',
		'size',
		'matrix'
	],
	#category : #Cannons
}

{ #category : #adding }
Matrix >> addElementAt: i and: j translate: t [
	| element |
	element := BlockElement new.
	element size: 50.
	element makeElementFrom: (self getSubmatrixAt: (j-1*size +i)) number:  (j-1*size +i).
	element translateBy: ((i-1)*50+ (5*i)+t)@((j-1)*50+ (5*j)+t).
	elements at:(j-1*size + i) put: element .
	panel add:element.
	panel addAll: (element innerElements)
]

{ #category : #adding }
Matrix >> addOnPanel: p [
	"self initialize ."
	panel := p.
	^ self
]

{ #category : #'as yet unclassified' }
Matrix >> getSubmatrixAt: p [
	 |subm i j row blocks elemNum|
	blocks  := 5.
	elemNum := matrix size / blocks.
	i := (p-1)//blocks * elemNum +1.
	j := (p-1)%blocks  *elemNum +1.
	subm := (Array new: elemNum ).
	1 to: elemNum do: [ :k|
		row := matrix at: i+k-1 .
		subm at:k put: (Array new:elemNum ).
		1 to:elemNum  do: [ :colNum|
			(subm at: k) at:colNum put: (row at: j+colNum-1) 
		 ].
		 ]
	.
	^subm
]

{ #category : #'as yet unclassified' }
Matrix >> initialShift [
]

{ #category : #'as yet unclassified' }
Matrix >> makeGrid: m translate: t [
	elements:= Array new: m*m.
	size := m.
	1 to: m do: [ :i |
			1 to: m do: [ :j|
					self addElementAt: i and: j translate: t
				 ] 
		 ] 
]

{ #category : #'as yet unclassified' }
Matrix >> readMatrix: filepath [ 
	| string mArray lines tokens|
	string := FileStream 
            readOnlyFileNamed: filepath 
            do: [:stream | lines:= (stream contents) string findTokens: String cr, String lf.
				mArray := (Array new:(lines size)).
				1 to: (lines size) do: [ :i| tokens := (lines at:i) splitOn: ' '.
				mArray at: i put: tokens ].
			^mArray 
		]. 
]

{ #category : #combining }
Matrix >> shift [ 
]

{ #category : #'as yet unclassified' }
Matrix >> switchElements: i and: j [
	panel addAnimation: (RTLinearMove new to: ((elements at: i)position ) during: 2 on: (elements at: j)).
]
