Class {
	#name : #BlockElement,
	#superclass : #RTElement,
	#instVars : [
		'block',
		'size',
		'innerElements'
	],
	#category : #Cannons
}

{ #category : #initialization }
BlockElement >> initialize [
	super initialize 
	"+ (RTBox new color: Color lightBlue;
	borderColor: Color black;
	borderWidth: 1;
	size: 50);
	model: '1';
	+ RTLabel "
]

{ #category : #accessing }
BlockElement >> innerElements [
	^innerElements 
]

{ #category : #'as yet unclassified' }
BlockElement >> makeElementFrom: b number: n [
block := b.
self
+ (RTBox new color: Color lightBlue;
	borderColor: Color black;
	borderWidth: 1;
	width: size;
	height: size);
	model: n";
	+ RTLabel" .
	shape := (RTBox new size: (size/2-6)).
	
	innerElements  := (Array new: (block size)*(block size)).
	
	  (1 to: (block size) do: [ :i|
			1 to: (block size) do: [ :j|
				innerElements at:(i-1*(block size)+j) put: (RTElement new + (RTBox new  width: size/(block size) -10;height: size/(block size) -10; borderColor: Color black; color: Color lightBlue );model:((block at:i) at:j); + (RTLabel color: Color black ) )

				 ]
		 ])
	.
	RTGridLayout new on: innerElements.
	RTNest new 
		on: self nest: innerElements.
	^ self
]

{ #category : #'as yet unclassified' }
BlockElement >> makeElementFrom: b number: n color: c [
block := b.
self
+ (RTBox new color: c;
	borderColor: Color black;
	borderWidth: 1;
	width: size;
	height: size);
	model: n";
	+ RTLabel" .
	shape := (RTBox new size: (size/2-6)).
	
	innerElements  := (Array new: (block size)*(block size)).
	
	  (1 to: (block size) do: [ :i|
			1 to: (block size) do: [ :j|
				innerElements at:(i-1*(block size)+j) put: (RTElement new + (RTBox new  width: size/(block size) -10;height: size/(block size) -10; borderColor: Color black; color: c );model:((block at:i) at:j); + (RTLabel color: Color black ) )

				 ]
		 ])
	.
	RTGridLayout new on: innerElements.
	RTNest new 
		on: self nest: innerElements.
	^ self
]

{ #category : #accessing }
BlockElement >> size: s [
 size := s
]
