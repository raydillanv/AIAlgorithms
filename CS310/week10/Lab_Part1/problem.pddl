(define (problem strathclyde-taxi-problem)
	(:domain strathclyde-taxis)
	(:objects
		tic barony_hall livingstone_tower royal_college graham_hills - location
		taxi_1 - taxi
		alice bob charlie - person
	)
	(:init
		(at-taxi tic) ; Taxi starts at TIC
		(at-person alice royal_college) ; Alice starts at Royal College
		(at-person bob livingstone_tower) ; Bob starts at Livingstone Tower
		(at-person charlie barony_hall) ; Charlie starts at Barony Hall
	)
	(:goal
		(and
			(at-person alice graham_hills) ; Alice wants to go to Graham Hills
			(at-person bob graham_hills) ; Bob wants to go to Graham Hills
			(at-person charlie graham_hills) ; Charlie wants to go to Graham Hills
		)
	)
)