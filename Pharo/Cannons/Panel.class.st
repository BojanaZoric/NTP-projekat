Class {
	#name : #Panel,
	#superclass : #Object,
	#instVars : [
		'builder',
		'ma',
		'mb',
		'myPanel',
		'size'
	],
	#category : #Cannons
}

{ #category : #drawing }
Panel >> draw [ 
	myPanel open
]

{ #category : #initialization }
Panel >> initialize [ 
	myPanel := RTView new.
	
]

{ #category : #'as yet unclassified' }
Panel >> ma [
	^ ma
]

{ #category : #'as yet unclassified' }
Panel >> makeAnimation [
| anim counter  steps|
anim := RTActiveAnimation new.
anim intervalInMilliseconds: 1000.
counter := 0.
steps := (size).
anim blockToExecute: [ 
	counter =0 ifTrue: [ ma initialShift value. mb initialShift value. counter := 1. anim intervalInMilliseconds: 3000 ] 
	ifFalse: [  ((counter > 0) and: (counter < size )) 
				  ifTrue: [ ma shift value. mb shift value. counter := counter+1  ]]
].

anim inView: myPanel.
]

{ #category : #'as yet unclassified' }
Panel >> makeCannons: n [

size := n.
mb := MatrixB new.
mb addOnPanel: (myPanel).
mb makeGrid: n translate: (0-n)*50. 
mb shift.


ma := MatrixA new.
ma addOnPanel: (myPanel).
ma makeGrid: n translate: n*50.
ma shift .
ma addBorderAt: 1 and:1. 


]

{ #category : #'as yet unclassified' }
Panel >> mb [
	^mb
]

{ #category : #'accessing ui' }
Panel >> myPanel [ 
	^ myPanel 
]

{ #category : #accessing }
Panel >> start: n [
	self makeCannons: n.
	self makeAnimation;
	draw 
]
