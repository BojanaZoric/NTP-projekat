Class {
	#name : #Panel,
	#superclass : #Object,
	#instVars : [
		'builder',
		'ma',
		'mb',
		'myPanel'
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
| anim counter |
anim := RTActiveAnimation new.
anim intervalInMilliseconds: 1000.
counter := 0.
anim blockToExecute: [ 
	counter =0 ifTrue: [ ma initialShift value. mb initialShift value. counter := 1. anim intervalInMilliseconds: 3000 ] 
				  ifFalse: [ ma shift value. mb shift value. counter := counter+1  ]
].
anim inView: myPanel.
]

{ #category : #'as yet unclassified' }
Panel >> makeCannons [

mb := MatrixB new.
mb addOnPanel: (myPanel).
mb makeGrid: 4 translate: -50. 
mb shift.


ma := MatrixA new.
ma addOnPanel: (myPanel).
ma makeGrid: 4 translate: 50.
ma shift .


]

{ #category : #'as yet unclassified' }
Panel >> mb [
	^mb
]

{ #category : #'accessing ui' }
Panel >> myPanel [ 
	^ myPanel 
]
